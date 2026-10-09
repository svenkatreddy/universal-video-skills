#!/usr/bin/env python3
"""Automated identity QA for generated video clips.

Triage, not a replacement for human review: extracts N frames per clip,
embeds each with CLIP, and measures cosine distance against a reference
(character sheet) embedding. Clips whose worst frame drifts too far FAIL
and go to human review; passes get a random-sample human spot check.

Usage:
    # 1. Calibrate once per character/project (no universal threshold exists):
    python3 scripts/identity_score.py --ref assets/reference.png \\
        --calibrate-good good1.jpg good2.jpg good3.jpg \\
        --calibrate-bad bad1.jpg bad2.jpg

    # 2. Score clips against the calibrated threshold:
    python3 scripts/identity_score.py --ref assets/reference.png \\
        --clips shot-*.mp4 --frames 12 --threshold 0.32 \\
        --out qa.jsonl

Requires: ffmpeg on PATH; Python deps: torch, open_clip_torch, Pillow.
    pip install torch open_clip_torch Pillow
(CPU works but is slow; CUDA recommended for batches of clips.)

Notes:
- CLIP measures overall visual similarity, not "is the ear the right shape".
  It catches gross drift (face/character swaps, morphing) reliably and
  subtle part-level defects (a shortened horn) sometimes. The failure
  taxonomy's manual gates still own the fine detail.
- Do NOT reuse face-recognition thresholds here: e.g. capy-video-gen-skill's
  0.40 pass mark is for VGG-Face embeddings on human faces. CLIP on a
  cartoon deity is a different space, so calibrate per project.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile


def need_deps():
    try:
        import torch  # noqa: F401
        import open_clip  # noqa: F401
        from PIL import Image  # noqa: F401
    except ImportError as e:
        sys.exit(
            f"missing dependency ({e}). Install the QA stack first:\n"
            "    pip install torch open_clip_torch Pillow\n"
            "CPU-only is fine for trying it out; expect ~1-2s per frame."
        )


def parse_args():
    ap = argparse.ArgumentParser(
        description="CLIP-embedding identity QA: score clip frames vs a reference image."
    )
    ap.add_argument("--ref", help="Reference image (character sheet).")
    ap.add_argument("--clips", nargs="*", default=[],
                    help="Clip files to score.")
    ap.add_argument("--frames", type=int, default=12,
                    help="Frames extracted per clip (default 12).")
    ap.add_argument("--threshold", type=float, default=None,
                    help="Max allowed worst-frame cosine distance. "
                         "If omitted, use --calibrate-* to find one.")
    ap.add_argument("--calibrate-good", nargs="*", default=[],
                    help="Frame images known to preserve identity.")
    ap.add_argument("--calibrate-bad", nargs="*", default=[],
                    help="Frame images known to break identity.")
    ap.add_argument("--out", default="identity-qa.jsonl",
                    help="JSONL results file (default identity-qa.jsonl).")
    ap.add_argument("--model", default="ViT-B-32",
                    help="open_clip model (default ViT-B-32).")
    ap.add_argument("--device", default=None,
                    help="torch device (default: cuda if available else cpu).")
    return ap.parse_args()


# ---- model (lazy: only imported when actually scoring) ----

_model = None


def get_model(model_name, device):
    global _model
    if _model is None:
        need_deps()
        import torch
        import open_clip
        device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        if device == "cpu":
            print("note: running on CPU, so scoring will be slow (~1-2s/frame).",
                  file=sys.stderr)
        cache = os.path.expanduser("~/.cache/clip")
        if not (os.path.isdir(cache) and os.listdir(cache)):
            print("first run: downloading CLIP weights (~350MB, cached afterwards)...",
                  file=sys.stderr)
        model, _, preprocess = open_clip.create_model_and_transforms(
            model_name, pretrained="openai", device=device)
        model.eval()
        _model = (model, preprocess, device)
    return _model


def embed(path, model_name="ViT-B-32", device=None):
    model, preprocess, device = get_model(model_name, device)  # need_deps() inside
    import torch
    from PIL import Image
    img = Image.open(path).convert("RGB")
    with torch.no_grad():
        vec = model.encode_image(preprocess(img).unsqueeze(0).to(device))
        vec = vec / vec.norm(dim=-1, keepdim=True)
    return vec[0].cpu()


def cos_distance(a, b):
    return float(1 - (a @ b).item())


# ---- frame extraction ----

def extract_frames(video, n, tmpdir):
    """Extract n evenly spaced frames; return list of paths."""
    r = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_format", video],
        capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffprobe failed on {video}")
    dur = float(json.loads(r.stdout)["format"]["duration"])
    paths = []
    for i in range(n):
        t = dur * (i + 0.5) / n
        out = os.path.join(tmpdir, f"f{i:03d}.jpg")
        r = subprocess.run(
            ["ffmpeg", "-y", "-v", "quiet", "-ss", f"{t:.2f}",
             "-i", video, "-frames:v", "1", "-q:v", "3", out],
            capture_output=True)
        if r.returncode != 0 or not os.path.exists(out):
            sys.exit(f"frame extraction failed for {video} at t={t:.2f}")
        paths.append((out, t))
    return paths


# ---- calibration ----

def calibrate(ref_vec, good, bad, model_name, device):
    def dists(paths):
        return sorted(cos_distance(ref_vec, embed(p, model_name, device))
                      for p in paths)
    gd, bd = dists(good), dists(bad)
    print(f"good distances (n={len(gd)}): "
          f"min {gd[0]:.3f}  max {gd[-1]:.3f}")
    print(f"bad  distances (n={len(bd)}): "
          f"min {bd[0]:.3f}  max {bd[-1]:.3f}")
    if gd[-1] < bd[0]:
        sug = (gd[-1] + bd[0]) / 2
        print(f"separable. Suggested threshold: {sug:.3f} "
              f"(midpoint between worst good and best bad).")
        print("Start there; tighten if bad clips pass, loosen if good clips fail.")
    else:
        print("WARNING: good/bad overlap, so no clean threshold. "
              "Pick one by trading off misses vs false alarms, or improve the "
              "reference (tighter crop on the character helps).")


# ---- main ----

def main():
    args = parse_args()

    if args.calibrate_good or args.calibrate_bad:
        if not (args.ref and args.calibrate_good and args.calibrate_bad):
            sys.exit("--calibrate needs --ref plus both --calibrate-good and "
                     "--calibrate-bad image lists.")
        ref_vec = embed(args.ref, args.model, args.device)
        calibrate(ref_vec, args.calibrate_good, args.calibrate_bad,
                  args.model, args.device)
        return

    if not args.ref or not args.clips:
        sys.exit("need --ref and --clips (or use --calibrate-*). "
                 "See --help.")
    if args.threshold is None:
        sys.exit("no --threshold given. Calibrate first:\n"
                 "  python3 scripts/identity_score.py --ref REF "
                 "--calibrate-good G... --calibrate-bad B...")

    ref_vec = embed(args.ref, args.model, args.device)
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        for clip in args.clips:
            if not os.path.isfile(clip):
                print(f"skip (not found): {clip}", file=sys.stderr)
                continue
            frames = extract_frames(clip, args.frames, tmp)
            per_frame = []
            for fp, t in frames:
                d = cos_distance(ref_vec, embed(fp, args.model, args.device))
                per_frame.append({"t": round(t, 2), "distance": round(d, 4)})
            worst = max(f["distance"] for f in per_frame)
            mean = sum(f["distance"] for f in per_frame) / len(per_frame)
            passed = worst < args.threshold
            res = {"clip": clip, "threshold": args.threshold,
                   "worst_frame_distance": round(worst, 4),
                   "mean_distance": round(mean, 4),
                   "pass": passed, "frames": per_frame}
            results.append(res)
            print(f"{'PASS' if passed else 'FAIL'}  {clip}  "
                  f"worst={worst:.3f} mean={mean:.3f}")

    with open(args.out, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    n_fail = sum(1 for r in results if not r["pass"])
    print(f"\n{len(results) - n_fail}/{len(results)} passed. "
          f"Results in {args.out}. Human-review all FAILs plus a random "
          f"sample of passes.")


if __name__ == "__main__":
    main()

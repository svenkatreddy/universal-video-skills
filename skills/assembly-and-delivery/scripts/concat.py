#!/usr/bin/env python3
"""Lossless-ish concat of AI video clips with pre/post verification.

Usage:
    python3 concat.py clip1.mp4 clip2.mp4 clip3.mp4 -o master.mp4

Checks every input with ffprobe (codec, resolution, fps, pix_fmt, audio),
concatenates with the ffmpeg concat demuxer (stream copy, no re-encode),
then verifies the output duration matches the sum of inputs.
Requires: ffmpeg, ffprobe on PATH.
"""

import argparse
import json
import subprocess
import sys
import tempfile
import os


def probe(path):
    r = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_streams", "-show_format", path],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        sys.exit(f"ffprobe failed on {path}:\n{r.stderr}")
    return json.loads(r.stdout)


def stream_info(path):
    data = probe(path)
    v = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in data["streams"] if s["codec_type"] == "audio"), None)
    if not v:
        sys.exit(f"{path}: no video stream found")
    dur = float(data["format"].get("duration", 0) or 0)
    audio = "none"
    if a:
        audio = (f'{a["codec_name"]} {a.get("sample_rate", "?")}Hz '
                 f'{a.get("channels", "?")}ch')
    return {
        "codec": v["codec_name"],
        "size": f'{v["width"]}x{v["height"]}',
        "fps": v.get("r_frame_rate", "?"),
        "pix_fmt": v.get("pix_fmt", "?"),
        "audio": audio,
        "duration": dur,
    }


def esc(path):
    """Escape a path for the concat demuxer file list."""
    return os.path.abspath(path).replace("'", "'\\''")


def main():
    ap = argparse.ArgumentParser(description="Verify and concatenate video clips.")
    ap.add_argument("clips", nargs="+", help="Input clips in order")
    ap.add_argument("-o", "--output", required=True, help="Output file")
    args = ap.parse_args()

    for c in args.clips:
        if not os.path.isfile(c):
            sys.exit(f"not found: {c}")
    out_abs = os.path.abspath(args.output)
    if out_abs in {os.path.abspath(c) for c in args.clips}:
        sys.exit("refusing: output must not be one of the inputs.")

    print("Probing inputs...")
    infos = [stream_info(c) for c in args.clips]
    ref = infos[0]
    ok = True
    for path, info in zip(args.clips, infos):
        mism = [k for k in ("codec", "size", "fps", "pix_fmt", "audio")
                if info[k] != ref[k]]
        flag = "OK " if not mism else "MISMATCH"
        if mism:
            ok = False
        print(f"  [{flag}] {path}: {info['size']} {info['codec']} "
              f"{info['fps']} {info['pix_fmt']} audio={info['audio']} "
              f"{info['duration']:.2f}s"
              + (f"  <-- differs in {', '.join(mism)}" if mism else ""))
    if not ok:
        sys.exit("\nInputs disagree. Transcode the odd ones out first "
                 "(see stitching.md), then re-run.")

    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        for c in args.clips:
            f.write(f"file '{esc(c)}'\n")
        listfile = f.name

    print("Concatenating...")
    r = subprocess.run(
        ["ffmpeg", "-y", "-fflags", "+genpts", "-f", "concat", "-safe", "0",
         "-i", listfile, "-c", "copy", args.output],
        capture_output=True, text=True,
    )
    os.unlink(listfile)
    if r.returncode != 0:
        sys.exit(f"ffmpeg concat failed:\n{r.stderr[-2000:]}")

    expected = sum(i["duration"] for i in infos)
    actual = stream_info(args.output)["duration"]
    print(f"Expected ~{expected:.2f}s, got {actual:.2f}s")
    if abs(expected - actual) > 0.5:
        sys.exit("Duration mismatch — inspect the output before using it.")
    print(f"Done: {args.output}")


if __name__ == "__main__":
    main()

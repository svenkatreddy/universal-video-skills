#!/usr/bin/env python3
"""Extract a timestamped contact sheet from a video clip.

Usage:
    python3 contact_sheet.py clip.mp4 -o sheet.jpg
    python3 contact_sheet.py clip.mp4 -o sheet.jpg --n 8
    python3 contact_sheet.py clip.mp4 -o sheet.jpg --times 0.5,3.0,7.5

Pulls frames (evenly spaced, or at given timestamps), labels each with its
timestamp, and tiles them into a grid. Requires: ffmpeg on PATH, PIL
(pip install pillow).
"""

import argparse
import math
import os
import subprocess
import sys
import tempfile

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Pillow required: pip install pillow")


def duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_format", path],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        sys.exit(f"ffprobe failed on {path}")
    import json
    return float(json.loads(r.stdout)["format"]["duration"])


def grab(path, t, out):
    r = subprocess.run(
        ["ffmpeg", "-y", "-v", "quiet", "-ss", str(t), "-i", path,
         "-frames:v", "1", "-q:v", "3", out],
        capture_output=True,
    )
    if r.returncode != 0 or not os.path.exists(out):
        sys.exit(f"frame grab failed at t={t}")


def positive_int(v):
    try:
        iv = int(v)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not an integer: {v!r}")
    if iv < 1:
        raise argparse.ArgumentTypeError("--n must be >= 1")
    return iv


def time_list(v):
    try:
        ts = [float(x) for x in v.split(",")]
    except ValueError:
        raise argparse.ArgumentTypeError(
            "--times must be comma-separated numbers")
    if not ts:
        raise argparse.ArgumentTypeError("--times must not be empty")
    return ts


def main():
    ap = argparse.ArgumentParser(description="Build a contact sheet from a clip.")
    ap.add_argument("video", help="Input video")
    ap.add_argument("-o", "--output", required=True, help="Output image")
    ap.add_argument("--n", type=positive_int, default=12,
                    help="Frame count (default 12)")
    ap.add_argument("--times", type=time_list,
                    help="Comma-separated timestamps instead of even spacing")
    ap.add_argument("--cols", type=int, default=4, help="Grid columns (default 4)")
    ap.add_argument("--thumb", type=int, default=320, help="Thumbnail width (default 320)")
    args = ap.parse_args()

    if not os.path.isfile(args.video):
        sys.exit(f"not found: {args.video}")
    dur = duration(args.video)
    times = (args.times if args.times
             else [dur * (i + 0.5) / args.n for i in range(args.n)])
    times = [min(max(t, 0), dur - 0.05) for t in times]

    thumbs = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, t in enumerate(times):
            fp = os.path.join(tmp, f"f{i:03d}.jpg")
            grab(args.video, t, fp)
            img = Image.open(fp).convert("RGB")
            w, h = img.size
            img = img.resize((args.thumb, int(h * args.thumb / w)))
            d = ImageDraw.Draw(img)
            d.rectangle([0, 0, 78, 20], fill=(0, 0, 0))
            d.text((4, 3), f"{t:.1f}s", fill=(255, 255, 0))
            thumbs.append(img)

    cols = args.cols
    rows = math.ceil(len(thumbs) / cols)
    tw, th = thumbs[0].size
    sheet = Image.new("RGB", (cols * tw, rows * th), (20, 20, 20))
    for i, th_ in enumerate(thumbs):
        sheet.paste(th_, ((i % cols) * tw, (i // cols) * th))
    sheet.save(args.output)
    print(f"Wrote {args.output}: {len(thumbs)} frames from {args.video} "
          f"({dur:.1f}s)")


if __name__ == "__main__":
    main()

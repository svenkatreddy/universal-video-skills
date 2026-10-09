# Stitching Clips

## Before you join anything

Run `ffprobe` on every clip. All clips must agree on:

- Codec (H.264 everywhere, ideally)
- Resolution (1920×1080 everywhere, not "mostly")
- Frame rate (24 or 30 — pick one per project)
- Pixel format (`yuv420p` for compatibility)
- Audio: sample rate and channel count, or no audio at all

One odd clip poisons the concat. Transcode the odd one out first:

```bash
ffmpeg -i odd.mp4 -c:v libx264 -pix_fmt yuv420p -r 30 -s 1920x1080 \
       -c:a aac -ar 48000 -ac 2 odd-fixed.mp4
```

## The concat

Use the concat demuxer (lossless, no re-encode) via `scripts/concat.py`:

```bash
python3 scripts/concat.py clip1.mp4 clip2.mp4 clip3.mp4 -o master.mp4
```

The script verifies each input with ffprobe, writes the file list, runs the
concat, then checks the output duration against the sum of inputs. If the
numbers don't add up, it tells you.

## Transitions

The concat demuxer does hard cuts only. For dissolves or fades between
specific clips, use `xfade` on those two clips first, then concat the result:

```bash
ffmpeg -i a.mp4 -i b.mp4 -filter_complex \
  "[0:v][1:v]xfade=transition=fade:duration=0.5:offset=7.5[v]" \
  -map "[v]" ab.mp4
```

Rules of thumb:

- **Hard cuts** between shots in a sequence. Default.
- **Fade through black** (0.3–0.5s) for time jumps and act breaks.
- **Dissolves** for memory, dreams, passage of time. Rarely for anything
  else.
- **No transition** is a transition. When in doubt, cut.

## Finishing

- **Title card:** 2–3 seconds, project style. Generate it or build it in
  ffmpeg (`drawtext`) — keep the font files in the project.
- **Watermark:** small, corner, semi-transparent, throughout. Burn it in on
  the master so every export inherits it.
- **Subtitles:** sidecar `.srt` for YouTube; burned-in for platforms that
  strip sidecars. Same source file either way
  (`../../dialogue-and-audio/references/subtitles.md`).
- **Credits card:** end card, 3–4 seconds. Who made it, with what, sources
  if the content needs them.

## The join check

After assembly, watch 2 seconds on each side of every cut and ask:

1. Does the geography connect? (No teleports.)
2. Does the light match? (No noon-to-midnight cuts unless intended.)
3. Does the audio bridge? (Room tone continuous, no clicks.)
4. Does the pace breathe? (Not every cut at the same rhythm.)

Fix the clip or the cut — never ship a join you flinched at.

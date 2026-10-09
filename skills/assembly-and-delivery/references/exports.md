# Platform Exports

One master, many shapes. The master is 16:9 at full quality; everything else
is derived. Never upscale, never export from an export.

## The master

- **Codec:** H.264 (`libx264`), `yuv420p`, for compatibility; H.265 if size
  matters more than compatibility.
- **Bitrate:** 12–20 Mbps for 1080p masters. Masters are for archiving and
  deriving — don't starve them.
- **Audio:** AAC, 48kHz, 320kbps stereo.

## Social crops

**9:16 (Shorts/Reels/TikTok).** Center-crop the 16:9 master:

```bash
ffmpeg -i master.mp4 -vf "crop=608:1080:656:0" -c:v libx264 \
       -b:v 8M -c:a aac short-916.mp4
```

But check every shot after cropping — the interesting thing is often not in
the center. For shots where it isn't, reframe per shot (crop offsets differ)
and concat the reframed clips. AI footage framed for 16:9 rarely survives a
blind center crop.

**1:1 (feed posts).** Same idea, square crop. Check faces.

**Bitrates for delivery:** 8–12 Mbps for 1080p uploads. Platforms recompress
anyway; give them enough to work with.

## Subtitles per export

- YouTube: upload the `.srt` sidecar.
- Shorts/Reels/TikTok: burn them in — these players are unreliable with
  sidecars, and most viewers watch muted.

## The export checklist

- [ ] Master plays end to end, no glitches at joins
- [ ] Each crop checked shot by shot (nothing important cropped out)
- [ ] Subtitles present and timed on every export
- [ ] Loudness sane on a phone speaker
- [ ] File names carry version and aspect: `night-market-v3-916.mp4`

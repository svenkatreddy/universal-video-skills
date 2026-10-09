# Subtitles

Subtitle everything you publish. Most viewers watch with sound off, many
watch in a second language, and platforms reward captioned video. This isn't
optional polish — it's distribution.

## SRT basics

```
1
00:00:06,000 --> 00:00:08,000
One bowl. Extra chili.

2
00:00:12,500 --> 00:00:15,000
You came all this way for noodles?
```

- **Timing:** start when the line starts, end when it ends, plus a breath.
  Never let a subtitle linger more than ~7 seconds or flash under 1.
- **Length:** max two lines, ~42 characters per line. Split long lines at
  natural pauses.
- **Speaker labels** only when needed: `[VENDOR]`, or a dash for the second
  speaker. Narration usually needs none.
- **Sound cues** in brackets for important non-dialogue audio: `[rain
  intensifies]`, `[bell dings]`. Sparingly.

## Workflow

1. Lock the edit first. Subtitles timed to a moving cut are wasted work.
2. Transcribe from the script, not from the audio — the script is the source
   of truth. Fix the script if the take deviated.
3. Time each cue to the final timeline. Most editors and ffmpeg can burn
   subtitles in or ship them as a sidecar `.srt`.
4. Watch once with sound off, reading only the subtitles. If the story
   holds, they're doing their job.

## Burned-in vs. sidecar

- **Sidecar `.srt`** (YouTube, most players): lets viewers toggle, gets
  indexed, survives re-encodes. Default choice.
- **Burned-in**: for platforms that strip sidecars, or stylized captions that
  are part of the design. Burn from the same SRT so there's one source of
  truth.

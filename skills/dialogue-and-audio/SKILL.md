---
name: dialogue-and-audio
description: "Dialogue, voiceover, subtitles, and mixing for AI video: TTS casting, per-line timing, SRT subtitles, loudness. Use when a video has spoken lines, narration, or needs its audio finished in post."
---

# Dialogue and Audio

AI video models are getting better at sound, but "better" still means
unreliable: dialogue lands on the wrong beat, lips don't match, ambience is
a guess. The professional default is to **treat generated audio as a scratch
track and finish sound in post.** Plan for it from the start and you'll never
be disappointed; depend on native audio and you will be, eventually.

## The workflow

1. **Write the dialogue for the ear.** Short lines, speakable words, timed to
   beats (`references/voiceover.md`). If a line can't be said in the seconds
   you gave it, rewrite the line, not the timing.
2. **Cast the voices.** One voice per speaker, locked for the project,
   same discipline as faces. Note pronunciation traps (names, invented words)
   before recording anything.
3. **Generate or record per line.** TTS or human, one file per line, named
   systematically. Per-line files make retakes and re-timing trivial.
4. **Subtitle everything.** SRT files, timed to the final cut
   (`references/subtitles.md`). Subtitles are accessibility, not decoration.
   Most viewers watch muted.
5. **Mix it.** Dialogue, music, effects balanced; loudness normalized for the
   delivery platform (`references/mix.md`).

## Rules that don't bend

- **Time the lines.** Every spoken line gets a start and end time in the
  shot-brief's beats. Untimed dialogue is a wish.
- **One voice per speaker, always.** Switching TTS voices mid-project is the
  audio version of face drift.
- **Write for speaking, not reading.** Read every line out loud before
  generating. If you stumble, the TTS will too.
- **Mute-test the cut.** Watch the whole video with sound off. If the story
  doesn't survive, the visuals aren't carrying their weight.
- **Keep the stems.** Dialogue, music, effects as separate tracks until
  final export. Baked-in mixes can't be fixed.

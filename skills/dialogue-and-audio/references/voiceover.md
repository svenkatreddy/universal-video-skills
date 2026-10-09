# Voiceover and Dialogue

## Writing lines that speak

- **Short.** Aim for under 10 words a line in fast cuts, under 20 in slow
  ones. Long lines don't fit short clips — do the math: conversational
  speech runs ~150 words a minute, so an 8-second clip holds ~20 words max,
  and that's wall-to-wall talking with no air.
- **Speakable.** No tongue-twisters, no nested clauses, no words you'd have
  to spell for someone. Contractions are your friend.
- **Timed.** Every line sits inside a beat: `6–8s, MARA (barely smiling):
  "One bowl. Extra chili."` The timing is part of the writing.
- **Read it aloud.** The oldest test in the book and still the best. If you
  run out of breath, cut words.

## Casting voices

- **One voice per speaker for the whole project.** Note the voice ID/name in
  the asset registry next to the character — voices are assets.
- **Match voice to face.** A 34-year-old woman doesn't get a teenage voice.
  Obvious, but TTS defaults skew young and it's easy to accept the default.
- **Narration vs. dialogue are different jobs.** Narration wants warmth and
  steadiness; dialogue wants character. Don't use the same voice for both
  unless the story says so.
- **Pronunciation traps.** Names, place names, invented words — test them
  first. Most TTS engines mangle the same things (foreign names, "th"
  sounds, unexpected stress). Keep a project pronunciation list: the word as
  written, and the respelling that actually sounds right. Fix the spelling in
  the TTS input only; keep true spellings in scripts and subtitles.

## Generating

- **One file per line.** `s03-mara-01.wav`, `s03-mara-02.wav`. Retakes are
  inevitable; per-line files make them surgical.
- **Generate at the project's pace.** If the line is timed 6–8s, the audio
  should land near 2 seconds, not 5. Adjust speed or rewrite — don't stretch
  in post unless you have to.
- **Keep a retake log.** Line ID, what was wrong, what changed. Voice
  sessions drift the same way faces do; the log is your continuity.

## Lip sync, honestly

True lip sync (mouth matching phonemes) is still unreliable in AI video.
Your options, in order of reliability:

1. **Don't show the mouth.** Voiceover narration over B-roll never
   mismatches.
2. **Keep the speaker small or moving.** Distance and motion hide sync
   errors.
3. **Short lines on close-ups.** Two seconds of dialogue can pass; ten
   seconds won't.
4. **Accept and design around it.** If the story needs long synced dialogue,
   that's a shot for real footage or careful post work — not a prompt tweak.

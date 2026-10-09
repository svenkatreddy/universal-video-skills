# Gemini / Veo (Google adapter)

_Last verified: 2026-10-08. Verify durations, resolutions, and pricing
against Google's current docs before planning._

## In one line

Google's video models (Veo line, via Gemini API / app). Strong on
instruction-following, native dialogue, and structured prompts.

## Prompt quirks

- Takes structured/JSON-style prompts unusually well. The JSON prompting
  reference was popularized largely on Veo-class models.
- Native dialogue and sound: specify speaker + line + language explicitly;
  it handles synced speech better than most, but still verify per line.
- Responds well to concrete cinematic tokens (stocks, focal lengths, named
  grades).
- Negative prompts: supported in some interfaces; otherwise fold into
  `Avoid:` inline.

## Hard limits

- Duration caps and max resolution vary by model version and tier. Verify.
- On-screen text remains unreliable; keep signage out of focus or composite
  in post.

## Good at / weak at

- Good at: dialogue scenes, following complex multi-element instructions,
  realistic lighting.
- Weak at: very long takes, exact object counts under motion, small text.

## Translating a shot-brief

- The shot-brief maps almost 1:1, so keep all eight slots.
- For pipelines, author in JSON and submit structured; for one-offs, prose
  is fine.
- Put dialogue in the beats with timestamps, not just in Audio. Temporal
  placement matters for sync.
- Keep the Preserve slot explicit; Veo follows "hold this constant"
  instructions well.

# Muse (Adapter)

_Last verified: 2026-10-08. Muse is Meta's AI assistant; its built-in media
generation is the target here, not a standalone video model page._

## In one line

Video generation as an agent tool: the assistant generates clips inside a
working session, so prompting, verification, and iteration happen in one
loop.

## Prompt quirks

- Short clips (around ~10 seconds) — plan in segments and stitch, don't
  wish for long takes.
- Works well from the shot-brief grammar in prose; keep prompts ASCII-only
  (non-ASCII filenames and text have caused upstream rejections).
- Reference images help continuity; pass the same character references
  every time.
- It can't hear audio or see motion the way you do — verify results with
  extracted frames, not assumptions.

## Hard limits

- Clip length caps around ~10s — verify current limits in-session; they
  change.
- Face identity across clips is weak: lean hard on the asset registry and
  verbatim descriptions.
- Assume no reliable native dialogue sync; plan voiceover in post.

## Good at / weak at

- Good at: quick iteration inside an agent session, following concrete
  visual instructions, stylized looks.
- Weak at: long takes, face lock across segments, readable on-screen text,
  complex multi-object physics.

## Translating a shot-brief

- Split anything over ~10s into segments first (story-and-shots does this
  naturally).
- Keep the beats tight: 2–3 timed chunks per clip max.
- Paste the negative block inline as an `Avoid:` line.
- After generation, extract frames at clip boundaries and check the joins
  before accepting the clip (video-qa).

# Sora (Adapter — OpenAI)

_Last verified: 2026-10-08. Verify durations, resolutions, and availability
against OpenAI's current docs before planning._

## In one line

OpenAI's video model. Known for long, coherent takes and strong
storyboard-style prompting.

## Prompt quirks

- Handles longer, more narrative prompts than most — you can brief a fuller
  scene, not just a shot.
- Storyboard/timeline-style input works well: describe the sequence, not
  just the frame.
- Remixing and extending clips is a core workflow: generate, then extend or
  re-cut rather than re-rolling from scratch.
- Negative prompting support varies by interface; inline `Avoid:` is the
  safe default.

## Hard limits

- Duration and resolution caps depend on model version and plan — verify.
- Complex multi-character interaction still drifts; keep casts small.

## Good at / weak at

- Good at: coherent longer shots, camera motion through space, stylized
  worlds.
- Weak at: exact text, precise object counts, photoreal faces in motion
  (improving, but verify).

## Translating a shot-brief

- You can merge 2–3 adjacent shot-briefs into one longer Sora prompt when
  the action is continuous — then split in post if needed.
- Lean on the storyboard: Sora rewards "and then" structure.
- Keep camera moves simple and motivated; it renders them cleanly.
- Still write the Preserve slot — coherence is good, not automatic.

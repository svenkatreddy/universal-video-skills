# Image-to-Video Prompting: The Subtraction Principle

Text-to-video and image-to-video need opposite prompting instincts. In T2V,
you describe everything: the model invents the frame from your words. In
I2V, the frame already exists. Every word you spend redescribing what's in
the anchor image is a word the model can use to *reinvent* it, which is
exactly how locked characters drift.

The rule: **in I2V, describe only what the image doesn't already show:
the motion.** Subtract everything static.

## What gets subtracted

| Shot-brief slot | T2V | I2V |
|---|---|---|
| Subject appearance | Full description | Omitted (locked by the image) |
| Setting | Full description | Omitted (locked by the image) |
| Style lens | Full tokens | Omitted (or one line if the model needs the nudge) |
| Camera | Framing + movement | Movement only (framing is in the image) |
| Beats | Timed action | Timed action: this is the prompt now |
| Audio | Full | Full (the image has no sound) |
| Preserve | Identity/geometry | Still critical: name what must not change *during* motion |
| Avoid | Full block | Full block |

What's left is a short, dense prompt: motion, camera move, timing,
audio, preserve, avoid. Shorter prompts, fewer reinventions.

## A worked example

Same Mara shot as T2V (`../../examples/shot-brief.md`), rewritten for I2V:

> From this still moment, motion begins: Mara weaves between the stalls
> (0–3s), slows at the dumpling cart as steam washes over her face (3–6s),
> then looks up into the lens and smiles, barely (6–8s). Camera: slow
> tracking move keeping pace on her left, locked horizon. Audio: sizzle and
> chatter, rain on canvas awnings. Preserve: Mara's face, copper bob, and
> olive bomber jacket exactly as in the anchor frame; three stalls on her
> right. Avoid: morphing faces, extra limbs, camera shake, slow motion.

Notice there's no "copper bob, olive bomber jacket" description. The image
has her. No market description either: the image is the market. The prompt
is motion plus constraints.

Opening phrases like "From this still moment," or "As motion begins,"
help: they tell the model to animate the frame, not reinterpret it.

## When to still describe

Subtract the obvious, not the ambiguous. If the anchor shows a stranger
half-hidden behind a stall and the story needs him, name him. The image
doesn't lock what it barely shows. If a prop matters and it's small or
occluded, call it out in Preserve. Subtraction is about not *repeating*
the image, not about withholding information the image lacks.

## I2V discipline

- **Anchor quality is the ceiling.** Sharp, well-lit, no text or logos in
  frame (text warps in motion), subject clearly visible. A weak anchor
  can't be prompted back to strength.
- **Under 5 seconds for identity-critical shots.** Consistency degrades
  toward the end of longer clips. For longer sequences, generate 5-second
  segments and use each clip's final frame as the next anchor.
- **Camera movement over subject movement for close-ups.** Orbit, push-in,
  and tracking are the most reliable I2V moves, because the subject stays locked
  while the camera does the work. Wild subject action is where drift starts.
- **Save the final frame of every segment.** It's the next shot's anchor.
  This is also how multi-shot continuity actually works in I2V pipelines.
- **One motion per clip.** Same rule as T2V camera moves: one clear action,
  timed in beats. Two actions in 5 seconds smear.

Inspired by the I2V workflow doctrine in 0xzgbot's hermes-media-skill-pack
(MIT), rewritten here in this pack's grammar.

---
name: video-prompt-craft
description: Write text-to-video and image-to-video prompts that hold up in real generation. Shot-brief grammar, JSON prompting, negative prompts, and failure-mode hardening. Use when drafting, reviewing, or fixing a video generation prompt for any model.
---

# Video Prompt Craft

Most bad AI video comes from bad prompts, not bad models. The usual failure is
vagueness: "a beautiful cinematic shot of a woman walking in Paris." That
sentence asks the model to invent the shot, the walk, the light, and the city.
It will invent all of them differently every time.

This skill teaches one habit: **say what the camera sees, beat by beat, and say
what it must not do.** Everything else is commentary.

## The workflow

1. **Brief it.** Write the prompt in the shot-brief grammar
   (`references/prompt-grammar.md`). Eight slots, no more. If a slot is empty,
   that's a decision you're handing to the model. Do it on purpose or fill it.
   For image-to-video, subtract instead: `references/i2v-prompting.md`.
2. **Consider JSON.** For pipelines, revisions, or multi-shot work, write the
   brief as JSON instead of prose (`references/json-prompting.md`). Same
   information, but diffable and harder to silently change between drafts.
3. **Harden it.** Add the negative prompt (`references/negative-prompts.md`)
   and walk the failure-mode list (`references/failure-modes.md`). Restrictions
   are cheap; reshoots are not.
4. **Adapt it.** Run the finished prompt through the target model's adapter
   (`../model-adapters/SKILL.md`). The grammar is universal; every model has
   quirks.

## Rules that don't bend

- **Concrete verbs beat adjectives.** "She strides" beats "she walks
  beautifully." "Rain hammers the awning" beats "a moody rainy atmosphere."
- **Counts and positions are load-bearing.** "Three seagulls, left to right"
  beats "some birds." Models drop or multiply anything you don't pin down.
- **One variable at a time.** When a result is wrong, change one slot and
  regenerate. Changing three things teaches you nothing.
- **Reuse character descriptions verbatim.** Paraphrasing a face between shots
  is how you get two different people. Copy-paste, don't rewrite. (Full
  discipline: `../character-consistency/SKILL.md`.)
- **Time the beats.** A 10-second clip needs its action budgeted in seconds,
  not vibes. If you can't split the action into timed chunks, the prompt isn't
  ready.

## When this skill is not enough

- Camera language (angles, moves, lenses): `../cinematic-direction/SKILL.md`
- Multi-shot structure, storyboards, review gates: `../story-and-shots/SKILL.md`
- Dialogue, voiceover, subtitles, mixing: `../dialogue-and-audio/SKILL.md`
- Stitching clips and exporting: `../assembly-and-delivery/SKILL.md`
- Checking the result: `../video-qa/SKILL.md`

---
name: model-adapters
description: Translate a finished shot-brief into per-model instructions for Muse, Gemini/Veo, Sora, Kling, Runway, Pika, Luma, and Hailuo. Constraint sheets, prompt quirks, and what to verify. Use after the prompt is written, before generating.
---

# Model Adapters

The shot-brief grammar is universal. Models are not. Each one has its own
duration caps, aspect ratios, prompt quirks, and failure patterns, and they
change every few months. This skill is the translation layer: finished brief
in, model-ready instructions out.

## The workflow

1. **Write the prompt model-agnostic first.** Finish the shot-brief
   (`../video-prompt-craft/`) completely before opening an adapter. Adapters
   translate; they don't write.
2. **Read the adapter for your target.** Each sheet covers: what the model is
   good at, prompt quirks that matter, hard limits, and how negatives and
   reference images work there.
3. **Apply the quirks, keep the story.** The beats, the camera, the Preserve
   slot. Those don't change. What changes is formatting and emphasis.
4. **Verify volatile specs.** Durations, resolutions, and prices move fast.
   Every sheet is dated; if the date is old, check the provider before
   planning around a number.

## The adapter list

| Adapter | File | Best for |
|---------|------|----------|
| Muse (Meta) | `references/muse.md` | Agent-driven generation inside Muse |
| Gemini / Veo (Google) | `references/gemini-veo.md` | Dialogue-heavy, JSON-structured prompts |
| Sora (OpenAI) | `references/sora.md` | Long coherent takes, storyboards |
| Kling | `references/kling.md` | Realistic motion, camera controls |
| Runway | `references/runway.md` | Stylized looks, creative tools |
| Pika | `references/pika.md` | Quick social clips, effects |
| Luma (Dream Machine) | `references/luma.md` | Natural camera motion |
| Hailuo / MiniMax | `references/hailuo.md` | Character acting, Chinese-language content |

## Adding an adapter

Copy `references/adapter-template.md`. One page max. Facts over adjectives,
dates on every number, and a clear line between "prompting advice" (durable)
and "current specs" (perishable). If you can't verify a spec, write "verify"
instead of guessing.

---
name: cinematic-direction
description: "Direct the look of AI video like a cinematographer: camera language, movement, lighting, color, and style lenses. Use when a prompt needs a real shot in it, not just a subject, or when results look flat and amateur."
---

# Cinematic Direction

AI video models know what things look like; they don't know what a *shot* is
unless you tell them. "A man in a cafe" gives you a man in a cafe. "Low-angle
medium shot, slow push in, man in a cafe, sodium streetlight through blinds"
gives you cinema. The difference is entirely in the directing vocabulary.

This skill is that vocabulary, organized the way a DP thinks: camera first,
then light, then the overall style.

## The workflow

1. **Pick the shot.** Framing + angle + movement from
   `references/camera-language.md`. One of each, stated plainly. If the camera
   doesn't move, write "locked off". Stillness is a decision.
2. **Light it.** Time of day, source, quality from
   `references/lighting-and-color.md`. Light does more for "cinematic" than
   any other single choice.
3. **Set the style.** A style lens from `references/style-lenses.md`: a film
   stock, an era, a director's grammar, stated as concrete tokens, not
   adjectives. One lens per project, used consistently.
4. **Write it into the brief.** Camera and light slots in the shot-brief
   grammar (`../video-prompt-craft/references/prompt-grammar.md`) are where
   this lives. This skill supplies the words; prompt-craft supplies the
   sentence.

## Rules that don't bend

- **Name the lens, don't describe it.** "35mm, f/2, Kodak Vision3 500T" beats
  "shot on film, cinematic look." Signature tokens (stocks, lenses, eras)
  are how models actually key into looks.
- **One move per shot.** Push in *or* orbit *or* track. Two moves in 8 seconds
  reads as indecision and usually smears.
- **Motivate the move.** The camera moves because the story does: push in on a
  realization, pull back on isolation, track with pursuit. Unmotivated movement
  is the fastest way to look like a screensaver.
- **Light is story.** Hard noon sun is not the same scene as blue-hour window
  light. Choose light for what the scene means, then let the model handle the
  photons.
- **Restraint reads as quality.** Fewer style tokens, used consistently, beat
  a soup of "cinematic ultra-detailed 8k masterpiece." Every adjective you cut
  makes the remaining ones stronger.

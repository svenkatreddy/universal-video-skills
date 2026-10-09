# Failure Modes and Prompt-Level Fixes

Every failure below is common, documented across models, and at least partly
fixable in the prompt. Fix in the prompt first; fix in post only what the
prompt can't reach.

## Faces and bodies

**Face drift across shots.** The same description renders as different people.
Fix: freeze one verbatim description, reuse it character-for-character, and
add a reference image (image-to-video or character reference where the model
supports it). Full system: `../../character-consistency/`.

**Hands.** Extra or melting fingers, especially in motion. Fix: keep hands
simple and occupied (`hands wrapped around the mug`), avoid close-ups of
gesturing hands, add `distorted hands` to negatives.

**Morphing mid-shot.** Features slide around during the clip. Fix: shorter
beats (≤5s chunks), `locked` camera language, `morphing face` in negatives.
Morphing gets worse with longer durations and complex motion — budget
accordingly.

## Text and detail

**Gibberish signage.** Any text in frame comes out scrambled. Fix: `no
readable text` in negatives, or keep signs out of focus / at an angle, or
composite real text in post. Don't fight this one; route around it.

**Object count drift.** Three stalls become two, then four. Fix: state exact
counts in the brief *and* in Preserve. "Three stalls on her right" is a
contract.

## Motion and physics

**Sliding feet / ice-skating.** Walking without weight. Fix: name the contact
(`boots strike wet asphalt`), slow the action down, avoid fast lateral moves.

**Background warping.** The set breathes around the subject. Fix: `locked off`
or slow camera moves, `warping background` in negatives, simpler backgrounds.

**Physics breaks.** Objects pass through each other, liquid behaves wrong.
Fix: simplify the interaction. One object, one action. Complex
object-interaction is still the frontier — design around it.

## Continuity

**Wardrobe and hair changes between shots.** Fix: asset registry
(`../../character-consistency/references/asset-registry.md`); cite the asset
ID in every brief; never paraphrase.

**Screen-direction flips.** Character exits right, enters left. Fix: state
screen direction per shot (`exits frame right`), keep a simple direction map
in your storyboard.

## Sound

**Dialogue mismatch.** Lips move wrong or the line lands on the wrong beat.
Fix: put dialogue in the timed beats (`4–6s: she says "..."`), keep lines
short, and verify the model actually does synced dialogue before depending on
it (adapters). Plan ADR/voiceover in post as the default, not the fallback
(`../../dialogue-and-audio/`).

## The meta-fix

When a shot fails twice with prompt changes, stop prompting and change the
plan: simplify the action, shorten the clip, switch to image-to-video with a
locked first frame, or cut around it. The prompt is not always the problem —
sometimes the shot is just beyond what current models do well. Knowing which
shots to avoid is a skill, not a surrender.

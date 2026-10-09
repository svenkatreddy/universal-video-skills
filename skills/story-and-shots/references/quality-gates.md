# Quality Gates

Gates are checkpoints with teeth: the project doesn't move forward until the
gate's question is answered. Two revision rounds max per gate. The third
round is never where the fix lives.

## The full pipeline

**Gate 1: Story.** Beats listed, each one a real change. Question: *does the
story work in one paragraph?* If not, no shot list yet.

**Gate 2: Style proof.** One establishing shot and one close-up generated
with the project's style lens. Question: *does the look hold across shot
sizes?* Fix the lens here, not after twenty generations.

**Gate 3: Asset lock.** Characters, products, and key props registered with
IDs and reference images (`../../character-consistency/`). Question: *can
every shot cite its assets instead of describing them?* No lock, no
generation.

**Gate 4: Shot list sign-off.** Beats → shots tabled, screen direction
marked, joins noted, risky shots flagged with a generation strategy.
Question: *could someone else generate this shot list and get your video?*
If not, it's not a plan yet.

**Gate 5: Per-shot review.** Each generated clip checked against its brief
(`../../video-qa/`). Question per clip: *does it do its story job?* Fix the
prompt (one variable at a time) or cut the shot. Don't accumulate
almost-good clips.

**Gate 6: Assembly review.** The cut watched end to end. Question: *does it
flow?* Pacing, transitions, audio, and credits get judged here, never shot
by shot.

## The beat card (anti-slideshow check)

Before generating a beat's shots, fill one card per beat:

- **Main moving thing:** (just one: the beat has a single visual protagonist)
- **Start state → end state:** (what visibly changes)
- **Camera move:** (the one move, motivated)
- **Failure risk:** (what will probably go wrong, and the mitigation)

A beat where nothing visibly changes is a slideshow slide, not a story beat.
Rewrite it or cut it. This card is the cheapest quality filter in the whole
pipeline.

## The fast track

For simple jobs (a product shot, an establishing clip, a test), skip to
this:

1. One shot-brief, fully written (prompt-craft).
2. Style lens line pasted in.
3. Negative block pasted in.
4. Generate, check against the brief, done.

The fast track is not sloppiness; it's the same discipline with the
paperwork removed. Use it whenever the job is one shot and no continuity.

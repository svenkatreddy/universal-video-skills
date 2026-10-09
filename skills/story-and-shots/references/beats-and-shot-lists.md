# Beats and Shot Lists

## Beats

A beat is the smallest unit of story: something changes. "Mara enters the
market" is not a beat. Nothing changed. "Mara decides to follow the stranger"
is a beat.

Write beats as one line each, in order. A 60-second video usually has 5–9
beats. More than that and you're cutting a trailer, not a story.

Example: a 45-second short:

1. Mara crosses the night market in the rain, hunting for someone.
2. She spots the stranger's red umbrella: he's here.
3. She follows; he turns a corner and vanishes.
4. The umbrella lies abandoned in an alley. It wasn't him.
5. She laughs at herself, and notices the dumpling cart guy watching her.
6. She sits down. "One bowl." Maybe the night isn't wasted.

Six beats, six changes. That's a story.

## Shot lists

Each beat becomes one to three shots. The shot list is a table, so keep it
tight:

| # | Beat | Shot | Camera | Duration | Notes |
|---|------|------|--------|----------|-------|
| 1 | 1 | Market establishing | Wide, slow crane down | 8s | Rain, neon, blue hour |
| 2 | 1 | Mara walking | Medium track, waist height | 8s | Asset: mara-01 |
| 3 | 2 | Red umbrella reveal | Push in on umbrella | 6s | Color pop: red vs teal |
| 4 | 3 | Follow through crowd | Handheld-ish track | 8s | Screen dir: L→R |
| 5 | 3 | Empty corner | Locked wide | 5s | Beat of absence |
| 6 | 4 | Umbrella in alley | Low angle close-up | 6s | Rain hammering it |
| 7 | 5 | Mara laughs | Medium close-up, push in | 8s | Performance shot |
| 8 | 6 | Two bowls, steam | Overhead, slow drift | 8s | Ending warmth |

Notes column carries the load: asset IDs, screen direction, color decisions,
the join into the next shot. The person (or agent) writing prompts works from
this table, not from the story paragraph.

## Shot-list discipline

- **One row per generation.** If a row needs two generations, it's two rows.
- **Screen direction is a column, not a memory.** Mark L→R or R→L per moving
  shot. Flips are the most common multi-shot bug and the easiest to prevent.
- **Note the join.** "Cut on her laugh to the bowls" or "match cut: umbrella
  red → lantern red." The assembly stage (`../../assembly-and-delivery/`)
  should never have to guess.
- **Mark the risky shots.** Image-to-video with a locked frame for the
  performance close-up; text-to-video is fine for the establishing wide. Risk
  noted early gets mitigated early.

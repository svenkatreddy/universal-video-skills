# Style Lenses

A style lens is the look of the whole project, decided once and applied to
every shot. Without one, each generation invents its own aesthetic and your
video looks like twelve different films spliced together.

## How to set one

Pick one lens. Write it as concrete tokens (stocks, eras, techniques, a
named grammar) and paste the same line into every brief. Example:

`Style: 1970s paranoia thriller: 35mm, natural light, zoom lenses, muted
warm grade, subtle grain.`

That's a lens. "Cinematic and moody" is not.

## Useful lens families

**Era looks.** 70s naturalism (zoom, available light, grain), 80s neon
(synth palette, haze, anamorphic), 90s indie (16mm, flat light, muted),
Y2K gloss (high contrast, saturated, music-video cutting).

**Film stocks.** Kodak Vision3 500T (warm tungsten night), Fuji 400H (soft
pastel daylight), Tri-X / HP5 (hard black-and-white), expired 35mm
(color shifts, unpredictability; use sparingly).

**Director grammars** (use as shorthand, not impersonation). Slow arthouse
(long takes, locked frames, natural light), kinetic action (whip pans, snap
zooms, hard cutting), documentary (handheld, available light, real locations),
noir (hard shadow, venetian blinds, wet streets).

**Animation and stylization.** Hand-drawn anime (cel shading, limited
animation holds), watercolor storybook, claymation (visible fingerprints,
stepped motion), pixel-art, paper-cutout. Stylization hides model weaknesses
well. Faces matter less when nobody's photoreal.

## Rules

- **One lens per project.** Changing lenses mid-video is how you get the
  twelve-films problem.
- **Write it down once, paste it everywhere.** The lens line is part of your
  project template, next to the negative-prompt block.
- **Test the lens before the story.** Generate one establishing shot and one
  close-up with the lens. If both look right, the lens holds. If not, fix the
  lens now, not after twenty shots.
- **Lenses are not adjectives.** Every lens must survive being read as
  instructions: stocks, focal lengths, light sources, grades. If a token
  doesn't change the image, cut it.

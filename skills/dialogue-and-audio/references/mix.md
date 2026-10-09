# Mixing

A mix is three things at the right levels: dialogue you can hear, music that
supports, effects that sell the world. Everything else is taste.

## The level hierarchy

1. **Dialogue on top.** Always intelligible, always. If music fights the
   line, the music loses — duck it (dip music ~6dB under dialogue) or cut it.
2. **Effects for reality.** Foley and ambience are what make AI footage feel
   physical: rain, footsteps, room tone. AI video often ships silent or with
   mushy generated ambience; laying real effects under it is the fastest
   realism upgrade available.
3. **Music for emotion.** Under everything, felt more than heard — until the
   montage or the title, when it leads.

## Practical steps

- **Start from silence.** Mute any model-generated audio first, then build:
  dialogue → ambience bed → foley → music. Generated audio is a reference,
  not a foundation.
- **Room tone is mandatory.** A bed of neutral ambience under the whole cut
  hides every edit point. Without it, cuts click.
- **Normalize loudness for the platform.** YouTube wants around −14 LUFS,
  broadcast −23/−24, social feeds are the wild west — aim for −14 and check
  on a phone speaker. If it works on a phone speaker, it works anywhere.
- **Check the ends.** Fades in and out on the master (even 10 frames) kill
  the two most amateur sounds in existence: the hard start and the clipped
  tail.

## Keep the stems

Export and archive dialogue, music, and effects as separate stems alongside
the master. The client will ask for a music-and-effects version, a clean
dialogue track, or a recut — and you'll be glad you kept them.

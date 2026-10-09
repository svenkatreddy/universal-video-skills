# Kling (Adapter)

_Last verified: 2026-10-08. Verify durations, resolutions, and pricing
against current docs before planning._

## In one line

Strong realistic motion and camera control; a favorite for
human movement and dynamic shots.

## Prompt quirks

- Camera-control features (in supported interfaces) take explicit move
  descriptions well, so use the camera-language vocabulary literally.
- Image-to-video is a strength: lock the first frame, then direct the
  motion. For tricky shots, generate the still first.
- Negative prompts supported in most interfaces. Use the project block.
- Prompt in the interface's expected language/format; check current docs.

## Hard limits

- Duration caps vary by model version, so verify. Plan multi-shot for anything
  longer.
- Text rendering unreliable, as everywhere.

## Good at / weak at

- Good at: realistic human motion, camera moves, action shots.
- Weak at: long dialogue sync, exact counts, tiny detail stability.

## Translating a shot-brief

- The Camera slot is load-bearing here. Write the one move precisely.
- Prefer image-to-video for performance shots: still first (matching the
  storyboard panel), then animate.
- Keep beats short; Kling rewards clear, simple action per chunk.

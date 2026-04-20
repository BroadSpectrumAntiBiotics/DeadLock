# Assets for Root-Sentry

This folder holds all audio and visual assets for the game.

## Folder Structure

- `audio/music/` — Background tracks (ideally short looping files, 1–3 minutes)
- `audio/sfx/`   — Short sound effects (virus alerts, shop sounds, damage, success, etc.)
- `graphics/ui/` — Terminal borders, frames, health bars, shop layout, etc.
- `graphics/endings/` — Art shown in good/bad endings
- `graphics/misc/` — Title screen, system logos, separators, etc.

## Accepted Formats

**Audio:**
- Preferred: `.ogg` or `.wav` (small file size)
- Also accepted: `.mp3`
- Keep music files under ~5 MB each

**Graphics:**
- Plain text files (`.txt`) containing ASCII or ANSI-colored art
- Use fixed-width font friendly art (max ~80–100 characters wide)
- You can include ANSI escape codes for color if desired

## How to Contribute

1. Add your files to the appropriate subfolder.
2. Open a Pull Request with a short description of what you added.
3. Update `ui.py` or create a small helper if new loading logic is needed (or just tell me the filenames).

All contributors will receive full credit in the README and in-game credits.

Thanks for helping make Root-Sentry feel more alive!
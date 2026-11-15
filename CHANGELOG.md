# Changelog

## 1.22.0

- MIDI controller: a Polyend Tracker running i2 DECK drives the hub from its HUB deck. Run, stop, clear, seeds, batch, results (step, keep, toss, save, send, upscale), 16 tool slots, aspect, quality presets and pinned looks on the pads; steps, CFG, denoise, seed, size and batch on the wheel, with an on-screen readout. Off until you turn it on in Settings; Chrome or Edge. Full map in [docs/MIDI.md](docs/MIDI.md).

## 1.21.1 (first public release)

- Opens with a Starter lineup of 25 tools; the rest are in Settings › Module Library.
- NVIDIA VFX nodes: RTX Fast Upscale (upscale, denoise, deblur) and RTX Video Finish (clean up, upscale, frame generation, SDR to HDR).
- Output folders start empty; set yours in Settings.
- Style tools pick from the LoRAs you have installed.
- "Where does this file go" hints now know every loader the hub uses.
- Fonts are embedded; the hub no longer calls Google Fonts.
- Optional server-side safety guard for shared ComfyUI machines (works with current async ComfyUI; skips negative prompts; reads text from string and primitive nodes).

# Changelog

## 1.23.0

- Download buttons for missing models. Wherever the hub says a model file is missing (Missing Model, Workflow Rejected, Check my install, the template library), **Download** saves it straight into ComfyUI's models folder, in the right subfolder, with progress, cancel and **Download all**. Pick the models folder once (Chrome or Edge); ComfyUI sees the file without a restart. **browser ↓** still saves through the browser.
- Install buttons for missing node packs, through ComfyUI Manager (3.x, and 4.x with or without its legacy UI). The hub looks up which pack provides each missing node, installs it, and offers **Restart ComfyUI**, then reconnects and re-checks. Packs the Manager can't install by name get a link to paste into Install via Git URL; nodes that come with a newer ComfyUI say so.
- Settings › **Downloads**: link or change the models folder, see whether ComfyUI Manager was found, and **Find what's missing** for every active tool at once (also on the Module Library as **Get missing**).
- A Downloads box at the bottom left shows progress and the restart button.

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

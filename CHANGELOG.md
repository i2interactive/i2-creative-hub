# Changelog

## 1.25.2

Fixes from the first real SenseNova renders (RTX 3070 Ti 8 GB, ComfyUI 0.46.3):

- **Illustrated rebuilt: write, then draw.** ComfyUI's interleave task drew one picture and stopped without writing a word on the int8 checkpoint: its built-in system prompt pushes the model to draw first, and the node has no way to change it. Illustrated now writes the answer with a marker for each picture, writes a one-line description per marker, draws each one like Create, and places the pictures where the markers were. Two steps with two pictures took 31 s.
- **Ask answers in words.** Generate Text now sends a text-only system prompt and a short "answer in words" line. Without them the model began a picture and returned nothing. When it still does (open-ended questions about an attached picture, like "describe this", are the weak spot), the panel says so and suggests asking a direct question. Think first is now off by default: the model writes about 6 words a second on 8 GB.
- Fixed: the answer panel showed Think's reasoning twice, because ComfyUI's SenseNova node reports its own text too. Only the tool's answer and reasoning outputs reach the panel now.
- Fixed: Think's picture was repeated as a thumbnail under the reasoning.
- Copy and Send to give plain text without picture markers.

## 1.25.1

Fixes from the first test of 1.25.0 on a real rig (ComfyUI 0.46.2):

- Fixed: on a fresh form, settings that depend on Mode were hidden until you changed Mode. SenseNova's Self-correction and Aspect Ratio were missing in Create, and Qwen Image 2.1's Aspect Ratio and Megapixels were missing too. Settings in More settings now read the Mode control even though it sits above them.
- Fixed: SenseNova showed settings that do nothing in the current mode (Turbo steps in Ask, self-correction passes in Think, Illustrated and Ask). A setting can now depend on more than one control.
- Fixed: SenseNova's answer panel showed text another tool had made, including text from an earlier session. It now shows only answers SenseNova wrote.

## 1.25.0

- New tool: **SenseNova U1.6** (Image, off by default; turn it on in Settings › Module Library, or pick Full studio). One 8B model that draws, reasons, writes and edits, built node-for-node from ComfyUI's two SenseNova templates. Needs ComfyUI 0.46 or newer. Five modes:
  - **Create**: a picture from your prompt. Words in quotes are drawn as written.
  - **Think**: the model reasons about the layout in text, then draws. Its reasoning shows next to the result.
  - **Illustrated**: the model writes an answer and draws pictures where they help (a step-by-step guide, a short comic, a scene in beats). The pictures appear inside the text, where the model put them. Up to 8 pictures; each one is another render.
  - **Ask**: answers in words, about up to three pictures if you add them. No image is rendered, so it's the quickest mode.
  - **Edit**: change the picture you upload, with up to two extra reference pictures.
  - **Self-correction** (Create and Edit): checks the picture against your prompt, flags garbled text, typos and wrong numbering, and redraws, up to five passes.
  - **Turbo** (8-step LoRA, CFG 1) or **Quality** (50 steps, CFG 4; the negative prompt only applies here). Any aspect from 21:9 to 9:16, 0.5–4 MP; it starts at 2 MP for 8 GB cards.
  - Words and reasoning come back next to the render, with Copy and Send to. Live, Night Shift and pipelines use it as a picture tool (Create or Think).
  - The templates' Qwen3.5-9B prompt rewriter (8.8 GB) is left out; ✦ Enhance does that job. Download buttons for both model files.
- Fixed: Template Import misread nodes with grow-as-you-connect inputs (TextGenerateV2's images, videos and audios). Their saved settings shifted by three, so Thinking came out off when the template had it on.

## 1.24.0

- A living background in place of flat black. **Flow** is a slow field that takes the colour of the channel you're on, bends around your pointer, quickens a little while you type or render, and blooms when a render lands. It draws at a fraction of screen size, drops to 15 fps during renders and 10 when you're idle, and stops when the tab is hidden; on an RTX 3070 Ti a Z-Image render took 6.7 s with it on and 6.4 s with it off (within run-to-run noise).
- **Image** backgrounds: choose a picture, use your latest render, drop an image on Settings › Background, or press **Set as background** on any render in the viewer. Dim, blur, slow drift and a touch of Flow on top. Pictures stay in the browser and are scaled to 2560 px.
- Panels turn to smoked glass over the background; **Panels** sets how solid they are. **Black** brings back the old look.
- The models-folder picker now says so when it can't open, instead of doing nothing.
- Fixed: tools were blocked with "Missing models" when the files were installed. The pre-render check compared some loaders against another loader's list (CLIPVisionLoader against text encoders, MoGe against upscalers), which stopped 3D Model on a working install.
- Fixed: Frame Interpolation picked a checkpoint (an LTX video model) as its interpolation model, because its list came from a guess on the field name. It now reads its own loader's list.
- Fixed: Stitch / Grid was rejected by current ComfyUI. Images loaded from the output folder now carry the `[output]` tag it needs.
- Fixed: Looks were added to the Describe tools' instruction (Qwen3-VL, Gemma), so they described a "streetwear poster" or refused. Looks now only touch image, video and audio prompts.
- Gemma 4 Vision writes up to 512 tokens by default (was 2048, which took over 10 minutes on 8 GB).

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

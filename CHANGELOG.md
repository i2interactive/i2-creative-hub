# Changelog

## 1.27.1

- Tool names drop the "i2": **Roto**, **Cutter**, **OMNI**, **SHOWRUNNER**, **MICRODRAMA** and **Agent** (was i2 Agent). Nothing else changes; saved settings and gallery items carry over.

## 1.27.0

Fixes and polish across the hub.

- **JUMP** button in the header opens the tool search (same as Ctrl+K).
- Uploads get a **✕ clear** button. Old upload previews are freed from memory when replaced or cleared.
- Toggles work from the keyboard (Tab, then Space or Enter) and announce their state to screen readers.
- Face Swap and MiniMax H3 Follow motion say "Upload a Source Face image first" or "Upload a Motion Video first" before anything is uploaded or queued, instead of failing in ComfyUI.
- Node Canvas accepts tools that take a picture only in some modes (Qwen Image Edit, MiniMax H3, SenseNova Edit) and switches them to that mode, as the Pipeline already did. Its tool lists leave out tools you have turned off, and the prompt box shows for any tool that has a prompt.
- Action Stage keeps your prompt, sliders, steps, engine, animation settings and last render when you leave the page and come back. Its render button is now the primary button.
- Stop now finds and cancels stuck Live Canvas and background runs.
- The system-stats timer stops with the rest of the telemetry when ComfyUI disconnects.
- Settings backups now include the background, Spectrum, LoRA trigger words, Camera Angle, Night Shift and Live Canvas settings.
- Fixed: Tools-channel accent colour (`--cat-prep`) was never defined, so i2 Roto showed no colour.
- The pixel font is embedded once instead of twice (about 34 KB smaller).

## 1.26.0

Five i2 tools, all in the Full studio profile. Each one runs the graph exactly as it was built in ComfyUI, with its controls brought into the hub.

- New tool: **i2 Roto** (Tools). AI rotoscoping for real footage up to 6K with LTX-2.5 Alpha Gen. Drop a clip, or give a path on the ComfyUI PC: a clip, a folder of frames, or a numbered sequence like `plate.####.exr`. You get a matte sequence on disk (PNG 16-bit, EXR half or TIFF 16-bit, optional RGBA) plus matte and comp QC videos and a report. It needs the [ComfyUI-i2-Roto](https://github.com/i2interactive/ComfyUI-i2-Roto) node pack and five LTX-2.5 files, all with Install and Download buttons. The Alpha Gen LoRA is gated on Hugging Face.
- New tool: **i2 Cutter** (Workflows). An assistant editor. Give it a footage folder, a music track (dropped in or a path) and a brief, one story beat per line. It cuts on the beat and gives you a preview, a storyboard, the cut list and download links for an FCP 7 XML (Premiere, Resolve), an EDL and a cut-list JSON. It needs the [ComfyUI-i2-Cutter](https://github.com/i2interactive/ComfyUI-i2-Cutter) node pack.
- New tool: **i2 OMNI** (Workflows). One idea, or a picture, gives you key art, a lens-finished frame, a cutout with alpha, a depth map, a contact sheet and a parallax move with a sound bed. The prompt it used shows next to the results.
- New tool: **i2 SHOWRUNNER** (Workflows). An idea becomes a short film: script (written by the LLM or pasted in), key art, a still per shot, camera moves, a title card, a score and a 3D scene of the key art.
- New tool: **i2 MICRODRAMA** (Workflows). Vertical micro-drama episodes with a narrator, captions and music. After each episode, **Carry into the next episode** fills in the story so far and the next episode number. The narrator needs the [ComfyUI-Qwen-TTS](https://github.com/flybirdxx/ComfyUI-Qwen-TTS) node pack (keep transformers below 5.0).
- In the three i2 workflows, switches you turn off drop out of the graph with their models. With sound off, Stable Audio never loads. With no picture, nothing is loaded from disk. The i2 look LoRA is used when it is installed; otherwise the graph runs on plain Z-Image Turbo.
- Models stored in subfolders are found by name. A graph that asks for `LTX\x.safetensors` runs whether your copy sits in `loras/` or `loras/LTX/`.
- Music and audio can be dropped on upload fields. They get a player instead of a broken thumbnail.
- Fixed: single-line text fields never showed. Face Swap's face indexes and Krea 2's LoRA trigger words are back.
- Fixed: Template Import misread hand-written workflow files whose widget inputs lack the editor's widget marker. Saved values shifted onto the wrong inputs. One of ComfyUI's own templates (Bria product holding) now keeps its image names too.

## 1.25.3

From a full check of the hub on an RTX 3070 Ti 8 GB (ComfyUI 0.46.3):

- **Motion Capture is much faster on phone footage.** The clip's frames are brought to 1280 px on the long side before tracking, and MoGe, which only supplies the camera's field of view, now reads the first frame instead of every frame. A 5-second 4K iPhone clip finished in under 6 minutes; before, the depth step alone was on course for about 18 minutes.
- **Video tools warn before a clip that won't fit in memory.** ComfyUI holds every frame of a clip, and of the result, in RAM. RTX Video Finish, Video Upscale, Frame Interpolation and Motion Capture now estimate that from the clip and ask before queueing when it's more than about 60% of your RAM. (An 89-second clip at 2× asked for 42 GB on a 34 GB PC.)

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

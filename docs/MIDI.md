# MIDI controller: i2 DECK

The hub can be driven from a Polyend Tracker running **i2 DECK** (the i2 interactive firmware for the Tracker). Its **HUB** deck sends USB MIDI: 48 pads, a wheel with seven modes. The hub listens with Web MIDI. It is off until you turn it on, it only receives, and nothing leaves your machine.

## Setup

1. Plug the Tracker into the computer by USB and open the **HUB** deck (i2 DECK home, screen button 3).
2. Open the hub in **Chrome or Edge**. Web MIDI needs the hub opened as a file or from `localhost` (Safari and Firefox can't do it here).
3. **MENU › Settings › MIDI controller (i2 DECK)** › **ON**. The browser asks once to allow MIDI devices; allow it.
4. The hub finds the Tracker by name (any input called Tracker, Polyend or i2 DECK). To use something else, pick it under **Input**. Unplugging and replugging is picked up on its own.
5. A **MIDI** light appears in the header: green = listening, grey = waiting for the Tracker, red = a problem (hover it, or read the card in Settings). Every message flashes it, and **Last message** in Settings shows what came in.

The setting is remembered and included in **Backup & restore**. If MIDI was blocked, allow MIDI devices in the browser's site settings (the icon left of the address) and turn it on again.

## The protocol (from the firmware)

Read from `core/interface/i2Deck/i2DeckApp.cpp` and `i2DeckDecks.cpp` (`kHub`), and checked against the firmware's host harness log (`tools/i2deck/host`).

- **Pads:** note on `90 nn 64` (velocity 100) when pressed, note off `80 nn 00` when released. `nn` is the pad number 0-47 on the Tracker's 12×4 grid, so a pad's note is `row × 12 + block × 4 + column` (block 0 = QUEUE, 1 = WORKFLOWS, 2 = SHAPE + QUALITY). The hub acts on note on.
- **Wheel:** control change `B0 cc vv` with `cc` = the selected wheel mode (1 STEPS, 2 CFG, 3 DENOISE, 4 SEED, 5 WIDTH, 6 HEIGHT, 7 BATCH; screen buttons 1-7 pick it), relative: `vv` 65 = one click up, 63 = one click down. A fast turn sends one message per click (up to 8 per wheel read). Shift does not change what the HUB deck sends.
- **Channel 1** (the HUB deck has one page; channel = page). The hub ignores other channels.
- The hub ignores notes at velocity 127: that is how the MIXER deck's Mackie Control buttons arrive on the same port, so switching decks never fires hub actions. CC 20 on channel 16 (the STATIC deck) is ignored too.

## Pads

"The open tool" is the tool page on screen. "The result" is the one open in the viewer, or else your newest render.

| Note | Pad | What the hub does |
| --- | --- | --- |
| 0 | RUN | Run the open tool (same as Ctrl+Enter). With Live on: keep the full-quality render. Night Shift: start the night. World Builder, Pipeline, Node Canvas, Action Stage, Live Canvas: their main run button. |
| 1 | STOP | Stop the render that is running; the rest of the queue carries on (the Skip button). Night Shift, World Builder: stop. |
| 2 | CLR | Cancel all: clear the queue and stop the current render. |
| 3 | AGN | Run the last tool you ran again with its current settings (goes back to that tool first). A random seed gives a new take; a locked seed repeats it. |
| 12 | SEED | Roll a fresh fixed seed on the open tool. With Live on: a new live seed. |
| 13 | LOCK | Seed lock toggle: random (0) → your last render's seed on this tool; fixed → random. |
| 14 | B1 | Make ×1 per run. |
| 15 | B4 | Make ×4 per run. |
| 24 | PRV | Open the viewer on the result, then step to the previous one. Night Shift page: move the take cursor back. |
| 25 | NXT | Same, next one (the viewer's → arrow). Night Shift page: move the take cursor on. |
| 26 | KEEP | Star the result. Night Shift page: ★ Keep the take. |
| 27 | TOSS | Take the result off the hub's list and unstar it; the file stays on disk. Night Shift page: ✕ Cut the take. |
| 36 | SAVE | Download the result. Night Shift page: the take under the cursor. |
| 37 | SEND | Put the result (pictures only) into the open tool as its source picture. Night Shift page: Use (open the take in its tool). |
| 38 | OPEN | Open the result in the viewer, or close the viewer. Night Shift page: open the take. |
| 39 | HOME | Close the viewer and go to the index. |
| 4-7, 16-19, 28-31, 40-43 | W1-W16 | Open a tool. Set each slot in Settings › MIDI › Workflow slots. A slot on Auto follows the channel guide order (Image, Video, Audio, Upscale, 3D, Tools, Workflows, Agent; the tools you have switched on). |
| 8 | 1:1 | Aspect ratio on the open tool: its Aspect Ratio list, or width and height at about the same pixel count (multiples of 64). |
| 9 | 16:9 | as above |
| 10 | 9:16 | as above |
| 11 | 4:3 | as above |
| 20 | DRFT | The tool's Quality preset **Draft**. |
| 21 | GOOD | The tool's Quality preset **Balanced**. |
| 22 | BEST | The tool's Quality preset **Max**. |
| 23 | UPSC | Send the result picture to **SeedVR2 Upscale** (or the first upscaler you have on) and open it, ready to RUN. |
| 32-35, 44-47 | S1-S8 | Turn a look on or off: the 1st to 8th **pinned** look that fits the open tool (pin looks in Prompt Lab › Looks). |

Pad layout on the Tracker (note numbers):

```
QUEUE                 WORKFLOWS             SHAPE + QUALITY
RUN  STOP CLR  AGN    W1   W2   W3   W4     1:1  16:9 9:16 4:3
 0    1    2    3      4    5    6    7      8    9    10   11
SEED LOCK B1   B4     W5   W6   W7   W8     DRFT GOOD BEST UPSC
 12   13   14   15     16   17   18   19     20   21   22   23
PRV  NXT  KEEP TOSS   W9   W10  W11  W12    S1   S2   S3   S4
 24   25   26   27     28   29   30   31     32   33   34   35
SAVE SEND OPEN HOME   W13  W14  W15  W16    S5   S6   S7   S8
 36   37   38   39     40   41   42   43     44   45   46   47
```

## Wheel

Each click changes the open tool's control and a readout shows what changed (for example `CFG 4.5`). Values stay inside the control's own range.

| CC | Mode | Per click |
| --- | --- | --- |
| 1 | STEPS | ±1 step |
| 2 | CFG | ± the control's step (0.5 on most sliders, 0.1 on plain number boxes) |
| 3 | DENOISE | ± the control's step (0.05) |
| 4 | SEED | ±1. From random (0), it starts at your last render's seed (or a new one) and locks it. |
| 5 | WIDTH | ±64 px. On tools without width and height: megapixels instead (± its step). |
| 6 | HEIGHT | ±64 px. Same fallback. |
| 7 | BATCH | ×1 → ×2 → ×4 (works anywhere) |

## Not mapped

- Anything on a page without that control: the readout says so ("Not on Z-Image Turbo", "No quality presets on Finish"). Nothing changes.
- RUN on the i2 Agent, Prompt Lab, Template Import, Gallery, Settings and the guide: nothing to run.
- UPSC and SEND on videos, audio and 3D results: pictures only (open Video Upscale with a W pad for video).
- The wheel on Live Canvas, World Builder and the other custom pages: they have their own controls.
- Nothing goes back to the Tracker. The HUB deck only shows how far you turned the wheel, not the hub's values, and doesn't light pads from the computer (the firmware lights pads from the host only on Mackie Control decks).

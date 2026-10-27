# i2 Safety Guard (optional, server side)

The Creative Hub's content filter runs in the browser. Anyone who controls the HTML file can change it, which is fine on your own machine. If other people use your ComfyUI (a studio box, a classroom, a kiosk), install this guard on the ComfyUI side as well. It checks every job before ComfyUI queues it, whichever app sent it: the hub, ComfyUI's own interface, or a direct API call.

## Install

1. Copy the `i2_safety_guard` folder into `ComfyUI/custom_nodes/`.
2. Restart ComfyUI. The console prints `[i2_safety_guard] active`.
3. On a shared machine, make the folder read-only for everyone but the admin.

## What it blocks

The same rules as the hub's built-in filter:

- sexual or explicit content,
- sexual or violent content alongside anything that can refer to minors,
- graphic violence and gore.

It reads every piece of text in the workflow, including text coming from string and primitive nodes. It skips negative prompts (text that says what to keep out, such as "nsfw, blurry") and file names. A blocked job is refused with a normal ComfyUI error that names the reason; nothing runs.

It works with current ComfyUI (async prompt validation) and older versions. If it can't hook in, it prints a warning instead of stopping ComfyUI.

## Remove

Delete the folder from `custom_nodes` and restart ComfyUI.

# Install guide

This gets the i2 interactive Creative Hub (1.21.1) running against your own ComfyUI. Plan on about an hour, most of it downloading models. You only need the models for the tools you use: every tool has a **Check my install** button that lists exactly what it's missing.

## 1. What you need

- Windows or Linux with an **NVIDIA GPU**. The hub was built on an RTX 3070 Ti (8GB) with 32GB of RAM. 8GB runs most tools; video and 3D are happier with 12GB or more.
- **ComfyUI 0.40 or newer** (portable, desktop or a git install). 0.37 is the minimum for Qwen Image 2.1; older versions lose a few tools, and the hub's front page names which.
- **Chrome or Edge.**
- Optional: **LM Studio** for the i2 Agent, Night Shift, Enhance, Variations and Breed.

## 2. Start ComfyUI so the hub can reach it

The hub runs in your browser, so ComfyUI has to allow it in. Add `--enable-cors-header` to the way you start ComfyUI:

- **Portable (Windows):** edit `run_nvidia_gpu.bat` and add it to the end of the `python` line:
  `.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-cors-header`
- **Git install:** `python main.py --enable-cors-header`
- **ComfyUI Desktop:** Settings › Server-Config › add `--enable-cors-header` under extra launch arguments, then restart.

Also useful: `--preview-method auto` shows step previews in the hub's monitor while a render runs.

## 3. Open the hub and link it

1. Download `i2-creative-hub.html` and double-click it (or drag it into Chrome or Edge).
2. Click **OFFLINE** at the top right. The default address is `http://127.0.0.1:8188`; change it if your ComfyUI runs elsewhere, then link.
3. The front page now shows your ComfyUI version and whether anything needs updating.
4. Optional: in **MENU › Settings**, paste your ComfyUI output folder (for example `D:/ComfyUI/output`). The World Builder XML export uses it so Premiere and Resolve find the clips without relinking.

## 4. Node packs

Most tools use only nodes that ship with ComfyUI. These need a custom node pack. Install them from **ComfyUI Manager** (search the name), restart ComfyUI, then press **Re-check install** in Settings.

| Pack (search in ComfyUI Manager) | Needed for | Notes |
| --- | --- | --- |
| **ComfyUI Nvidia VFX Nodes** | RTX Fast Upscale, RTX Video Finish | Needs an RTX card and a CUDA 13 build of PyTorch. Frame generation needs an RTX 40-series or newer. |
| **WAS Node Suite** | Finish (bloom, grain, chromatic aberration, levels) | |
| **Radiance** | Finish (grade, white balance, film grain) | |
| **ComfyUI-Spectrum-MiniMax-H3** (optional) | MiniMax H3 speed-up switch | About 30% faster H3. The switch appears in More settings once it's installed. [GitHub](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) |
| **ReActor** | Face Swap (off by default) | |
| Tripo, Sharp and GeomPack nodes | Gaussian Splats (off by default) | Use ComfyUI Manager › Install Missing Custom Nodes on the template. |
| Searge and Qwen multi-angle camera nodes | Camera Angle (off by default) | Same as above. |

If a tool needs a node you don't have, the hub stops before anything is queued and names the missing node.

## 5. Models

Put each file in the folder shown, inside your ComfyUI folder (for example `ComfyUI/models/diffusion_models`). After adding files, press **Re-check install** in Settings (or reconnect) and they show up.

Most links go to the official Comfy-Org repackaged files. Where a tool offers variants (bf16 or int8, for example), you only need the one you pick.

### Starter tools

| File | Put it in | Needed for | Get it |
| --- | --- | --- | --- |
| `birefnet.safetensors` | `models/background_removal` | 3D Model; Background Remover | [download](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |
| `sam3.1_multiplex_fp16.safetensors` | `models/checkpoints` | Motion Capture | [download](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) |
| `sdpose_wholebody_fp16.safetensors` | `models/checkpoints` | Image Maps (only with Pose); MiniMax H3 (only with Follow motion) | [download](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) |
| `stable_audio_3_medium_base.safetensors` | `models/checkpoints` | Stable Audio 3 | [download](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/checkpoints/stable_audio_3_medium_base.safetensors) |
| `yue2_3b_int8_convrot.safetensors` | `models/checkpoints` | Music | [download](https://huggingface.co/Comfy-Org/YuE2/resolve/main/checkpoints/yue2_3b_int8_convrot.safetensors) |
| `dino_v3_L_naf_fp32.safetensors` | `models/clip_vision` | 3D Model | [download](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/clip_vision/dino_v3_L_naf_fp32.safetensors) |
| `sam_3d_body_dinov3_bf16.safetensors` | `models/detection` | Motion Capture | [download](https://huggingface.co/Comfy-Org/sam-3d-body/resolve/main/detection/sam_3d_body_dinov3_bf16.safetensors) |
| `acestep_v1.5_turbo.safetensors` | `models/diffusion_models` | Music (only with Quick (ACE-Step)) | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) |
| `fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors` | `models/diffusion_models` | MiniMax H3 (only with Fast) | [download](https://huggingface.co/FastVideo/FastVideo-FastH3-Comfy/resolve/main/diffusion_models/fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors) |
| `krea2_turbo_fp8_scaled.safetensors` | `models/diffusion_models` | Krea 2 Turbo | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_fp8_scaled.safetensors) |
| `krea2_turbo_int8_convrot.safetensors` | `models/diffusion_models` | Krea 2 Turbo (only with int8 (low VRAM)) | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_int8_convrot.safetensors) |
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `models/diffusion_models` | MiniMax H3 | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) |
| `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | `models/diffusion_models` | MiniMax H3 (only with Follow motion, From references) | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) |
| `pixal3d_int8_convrot.safetensors` | `models/diffusion_models` | 3D Model | [download](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/diffusion_models/pixal3d_int8_convrot.safetensors) |
| `pixal3d_multiview_int8_convrot.safetensors` | `models/diffusion_models` | 3D Model (only with Turnaround sheet) | [download](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/diffusion_models/pixal3d_multiview_int8_convrot.safetensors) |
| `qwen_image_2.1_int8_convrot.safetensors` | `models/diffusion_models` | Qwen Image 2.1 | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) |
| `qwen_image_edit_2509_int8_convrot.safetensors` | `models/diffusion_models` | Image Maps | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/diffusion_models/qwen_image_edit_2509_int8_convrot.safetensors) |
| `rt_detr_v4-x-hgnet_fp32.safetensors` | `models/diffusion_models` | Image Maps (only with Pose); MiniMax H3 (only with Follow motion); Motion Capture | [download](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp32.safetensors) |
| `seedvr2_3b_int8_convrot.safetensors` | `models/diffusion_models` | SeedVR2 Upscale; Video Upscale (only with AI detail (SeedVR2)) | [download](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) |
| `z_image_turbo_bf16.safetensors` | `models/diffusion_models` | Composition & Style; Creative Upscale; Z-Image Turbo | [download](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `z_image_turbo_int8_convrot.safetensors` | `models/diffusion_models` | Z-Image Turbo (only with int8 (low VRAM)) | [download](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_int8_convrot.safetensors) |
| `marigold_v2_albedo_conditioning.safetensors` | `models/embeddings` | Image Maps (only with Albedo (true color)) | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/embeddings/marigold_v2_albedo_conditioning.safetensors) |
| `marigold_v2_depth_conditioning.safetensors` | `models/embeddings` | Image Maps | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/embeddings/marigold_v2_depth_conditioning.safetensors) |
| `marigold_v2_normals_conditioning.safetensors` | `models/embeddings` | Image Maps (only with Surface normals) | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/embeddings/marigold_v2_normals_conditioning.safetensors) |
| `moge_2_vitl_normal_fp16.safetensors` | `models/geometry_estimation` | 3D Model; Motion Capture | [download](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) |
| `marigold_v2_albedo.safetensors` | `models/loras` | Image Maps (only with Albedo (true color)) | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/loras/marigold_v2_albedo.safetensors) |
| `marigold_v2_depth_log_stage2.safetensors` | `models/loras` | Image Maps | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/loras/marigold_v2_depth_log_stage2.safetensors) |
| `marigold_v2_normals.safetensors` | `models/loras` | Image Maps (only with Surface normals) | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/loras/marigold_v2_normals.safetensors) |
| `minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors` | `models/model_patches` | MiniMax H3 (only with Follow motion) | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/model_patches/minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors) |
| `Z-Image-Turbo-Fun-Controlnet-Union.safetensors` | `models/model_patches` | Composition & Style | [download](https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union/resolve/main/Z-Image-Turbo-Fun-Controlnet-Union.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `models/text_encoders` | MiniMax H3 | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `qwen3vl_4b_fp8_scaled.safetensors` | `models/text_encoders` | Krea 2 Turbo; Qwen3-VL Describe | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) |
| `qwen3vl_8b_int8_convrot.safetensors` | `models/text_encoders` | Qwen Image 2.1 | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| `qwen_0.6b_ace15.safetensors` | `models/text_encoders` | Music (only with Quick (ACE-Step)) | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) |
| `qwen_3_4b.safetensors` | `models/text_encoders` | Composition & Style; Creative Upscale; Z-Image Turbo | [download](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `qwen_4b_ace15.safetensors` | `models/text_encoders` | Music (only with Quick (ACE-Step)) | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) |
| `t5gemma_b_b_ul2.safetensors` | `models/text_encoders` | Stable Audio 3 | [download](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/text_encoders/t5gemma_b_b_ul2.safetensors) |
| `4x-UltraSharp.safetensors` | `models/upscale_models` | Video Upscale (only with 4x-UltraSharp.safetensors) | [download](https://huggingface.co/Kim2091/UltraSharp/resolve/main/4x-UltraSharp.safetensors) |
| `RealESRGAN_x4plus.safetensors` | `models/upscale_models` | Creative Upscale; Video Upscale | [download](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged/resolve/main/RealESRGAN_x4plus.safetensors) |
| `RealESRGAN_x4plus_anime_6B.safetensors` | `models/upscale_models` | Video Upscale (only with RealESRGAN_x4plus_anime_6B.safetensors) | [OpenModelDB (upscalers)](https://openmodeldb.info/) |
| `ace_1.5_vae.safetensors` | `models/vae` | Music (only with Quick (ACE-Step)) | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) |
| `ae.safetensors` | `models/vae` | Composition & Style; Creative Upscale; Z-Image Turbo | [download](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors?download=true) |
| `ema_vae_fp16.safetensors` | `models/vae` | SeedVR2 Upscale; Video Upscale (only with AI detail (SeedVR2)) | [search Hugging Face](https://huggingface.co/models?search=ema_vae_fp16) |
| `marigold_v2_albedo_vae.safetensors` | `models/vae` | Image Maps (only with Albedo (true color)) | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/vae/marigold_v2_albedo_vae.safetensors) |
| `marigold_v2_depth_log_stage2_vae.safetensors` | `models/vae` | Image Maps | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/vae/marigold_v2_depth_log_stage2_vae.safetensors) |
| `marigold_v2_normals_vae.safetensors` | `models/vae` | Image Maps (only with Surface normals) | [download](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/vae/marigold_v2_normals_vae.safetensors) |
| `minimax_h3_audio_vae_fp32.safetensors` | `models/vae` | MiniMax H3 | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) |
| `minimax_h3_video_vae_int8_convrot.safetensors` | `models/vae` | MiniMax H3 | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) |
| `qwen_image_2.1_vae_bf16.safetensors` | `models/vae` | Qwen Image 2.1 | [download](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) |
| `qwen_image_vae.safetensors` | `models/vae` | Krea 2 Turbo | [download](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) |
| `trellis_2_shape_vae_bf16.safetensors` | `models/vae` | 3D Model | [download](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_shape_vae_bf16.safetensors) |
| `trellis_2_texture_vae_bf16.safetensors` | `models/vae` | 3D Model | [download](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_texture_vae_bf16.safetensors) |

### Tools that are off by default

| File | Put it in | Needed for | Get it |
| --- | --- | --- | --- |
| `dino_v3_vit_h.safetensors` | `models/clip_vision` | Gaussian Splats (only with Tripo Splat) | [download](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/clip_vision/dino_v3_vit_h.safetensors) |
| `anima-base-v1.0.safetensors` | `models/diffusion_models` | Anima | [download](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) |
| `anima-preview2.safetensors` | `models/diffusion_models` | Anima (only with anima-preview2.safetensors) | [search Hugging Face](https://huggingface.co/models?search=anima-preview2) |
| `mage_flow_edit_turbo_int8_convrot.safetensors` | `models/diffusion_models` | Mage Flow Edit | [download](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_edit_turbo_int8_convrot.safetensors) |
| `mage_flow_turbo_int8_convrot.safetensors` | `models/diffusion_models` | Mage Flow Turbo | [download](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_turbo_int8_convrot.safetensors) |
| `triposplat_fp16.safetensors` | `models/diffusion_models` | Gaussian Splats (only with Tripo Splat) | [download](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/diffusion_models/triposplat_fp16.safetensors) |
| `GFPGANv1.4.pth` | `models/facerestore_models` | Face Swap | see the ReActor install notes |
| `film_net_fp16.safetensors` | `models/frame_interpolation` | Frame Interpolation | [download](https://huggingface.co/Comfy-Org/frame_interpolation/resolve/main/frame_interpolation/film_net_fp16.safetensors) |
| `inswapper_128.onnx` | `models/insightface` | Face Swap | see the ReActor install notes |
| `krea2_style_reference.safetensors` | `models/loras` | Krea 2 Style Reference | [download](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/loras/krea2_style_reference.safetensors) |
| `gemma4_e4b_it_fp8_scaled.safetensors` | `models/text_encoders` | Gemma 4 Vision | [download](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) |
| `qwen3vl_4b_bf16.safetensors` | `models/text_encoders` | Mage Flow Edit; Mage Flow Turbo | [download](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) |
| `qwen_3_06b_base.safetensors` | `models/text_encoders` | Anima | [download](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) |
| `4x-UltraSharp.pth` | `models/upscale_models` | Sharpen Upscale (only with 4x-UltraSharp.pth) | [OpenModelDB (upscalers)](https://openmodeldb.info/) |
| `4x_NMKD-Siax_200k.pth` | `models/upscale_models` | Sharpen Upscale (only with 4x_NMKD-Siax_200k.pth) | [OpenModelDB (upscalers)](https://openmodeldb.info/) |
| `flux2-vae.safetensors` | `models/vae` | Gaussian Splats (only with Tripo Splat) | [download](https://huggingface.co/Comfy-Org/Lens/resolve/main/vae/flux2-vae.safetensors) |
| `mage_flow_vae_bf16.safetensors` | `models/vae` | Mage Flow Edit; Mage Flow Turbo | [download](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) |
| `triposplat_vae_decoder_fp16.safetensors` | `models/vae` | Gaussian Splats (only with Tripo Splat) | [download](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/vae/triposplat_vae_decoder_fp16.safetensors) |

**LoRAs** go in `models/loras`. The LoRA Stack on each tool lists what you have, and the hub reads trigger words from the files where it can. A speed LoRA made for a tool's model (for example `…lightning…8steps`) is used automatically for Live drafts. The camera dial on Qwen Image 2.1 needs the [Multiple-Angles LoRA](https://huggingface.co/akhaliq/Qwen-Image-2.1-Multiple-Angles-LoRA).

## 6. LM Studio (optional)

The i2 Agent, Night Shift, prompt Enhance, Variations and Breed use a local LLM through LM Studio.

1. Install [LM Studio](https://lmstudio.ai).
2. Open the hub's **i2 Agent** page. The LM Studio panel there can download and load the recommended model (Qwen3.5 4B) in one click.
3. In LM Studio, go to **Developer › Server Settings** and turn on **Enable CORS**. Then start the server (default port 1234). Tick "Run the LLM server on login" if you want it always on.
4. Any OpenAI-compatible server works too: set the address, model name and key under **Connection settings** on the Agent page.

Tips:
- A model that can see images (Qwen3.5 can) lets Night Shift review its own takes. Without one, it steers from the prompts and your picks.
- **Step aside for heavy renders** (on by default) unloads the LLM before big jobs so ComfyUI gets the whole card, then reloads it.
- If you use a "thinking" model and see "the model did not answer in JSON", switch off thinking for that model in LM Studio or pick a non-thinking model.

## 7. Troubleshooting

- **The status stays red.** Check that ComfyUI is running, the address matches, and you started it with `--enable-cors-header`.
- **"Model not found".** Press **Check my install** on that tool. It names the file and the folder it goes in.
- **Out of memory.** Turn on **Low VRAM** mode in Settings, lower the size or steps, or use the int8 variant. When a render runs out of memory, the hub offers to free VRAM and retry.
- **A tool needs a newer ComfyUI.** The front page lists which tools need which version. Update, then press **Re-check install**.
- **RTX nodes won't load.** The Nvidia VFX pack needs a CUDA 13 build of PyTorch in the same Python that runs ComfyUI.
- **HDR video looks flat.** HDR files are BT.2020 HLG or PQ. Players without HDR show them washed out; grade them on an HDR timeline.

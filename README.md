# ModelScope Text2Video WebUI

Dirt simple Gradio powered WebUI for https://modelscope.cn/models/damo/text-to-video-synthesis/summary

# Linux Usage

- Install Python 3.7 (or 3.10 or whatever idk it's probably fine)
- Run `./start.sh`
- If something breaks in install re-run `./install.sh`
- Wait a while, it installs a ton of python packages then downloads like 20 gigs worth of random models
    - You might need to restart it a few times, it will randomly crash because they have server issues I guess.
- It will tell you the URL of a WebUI to connect to. Open that in your browser.
- Type prompts, hit generate, enjoy.

# Notes

- Some files wind up in `/tmp`
- Some model files for some reason wind up in your home directory at `~/.cache/modelscope/`
- Outputs will be stored in `./outputs/`
- Takes about 20 seconds to generate a video on an RTX 3090
- Uses about 16 GiB of VRAM

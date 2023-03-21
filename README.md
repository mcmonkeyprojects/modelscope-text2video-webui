# ModelScope Text2Video WebUI

Dirt simple Gradio powered WebUI for https://modelscope.cn/models/damo/text-to-video-synthesis/summary

# Usage

- Install Python 3.7 (or 3.10 or whatever idk it's probably fine)
- Run the program
    - For Windows, double-click `start.bat`
        - If something breaks in install, delete `venv` and run `start.bat` again
    - For Linux, run `./start.sh`
        - If something breaks in install, run `./install.sh`
- Wait a while, it installs a ton of python packages then downloads like 20 gigs worth of random models
    - You might need to restart it a few times, it will randomly crash because they have server issues I guess.
- Open <http://localhost:7860/> in your browser.
- Type prompts, hit generate, enjoy.

# Notes

- Some files wind up in `/tmp`
- Some model files for some reason wind up in your home directory at `~/.cache/modelscope/`
- Outputs will be stored in `./outputs/`
- Takes about 20 seconds to generate a video on an RTX 3090
- Uses about 16 GiB of VRAM

# Licenses

Code in this repo is MIT (do whatever ya want with it), modelscope is [Apache2](https://github.com/modelscope/modelscope/blob/master/LICENSE), the model itself has [its own license](https://modelscope.cn/models/damo/text-to-video-synthesis/summary). Other licenses from [Gradio](https://github.com/gradio-app/gradio/blob/main/LICENSE) and other upstream python libs apply however relevant.

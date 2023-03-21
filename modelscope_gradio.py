from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys
import shutil, time, random, torch, os, re
import gradio as gr

# Load model
preLoadTime = time.time()
pipe = pipeline('text-to-video-synthesis', 'damo/text-to-video-synthesis')
print(f"Loaded model in {time.time() - preLoadTime} seconds")

# Prep
if not os.path.exists("./output/"):
    os.makedirs("./output/")

# Main code
def generate(prompt: str, seed: int):
    # Generate
    if seed == -1:
        seed = random.randint(0, 100000)
    torch.manual_seed(seed)
    start_time = time.time()
    tempOutPath = pipe({'text': prompt})[OutputKeys.OUTPUT_VIDEO]
    genTime = time.time() - start_time
    # Save
    actualOutPath = "./output/" + re.sub("[^a-zA-Z0-9_ ]", "", prompt)
    if hasattr(os, 'statvfs'):
        max_name_len = os.statvfs("./output/").f_namemax
        actualOutPath = actualOutPath[:max_name_len - 5]
    actualOutPath += ".mp4"
    shutil.copy(tempOutPath, actualOutPath)
    # Report
    print(f"Generated video, saved at {actualOutPath}, took {genTime} seconds")
    return actualOutPath, f"Prompt = `{prompt}`, seed = `{seed}`, out-path = `{actualOutPath}`, generation-time = `{genTime}` seconds"

# Setup webapp
with gr.Blocks() as webapp:
    prompt = gr.Text(label="Prompt", placeholder="Text2Video prompt")
    with gr.Row():
        seed = gr.Number(label="Seed", value=-1, info="-1 means randomize")
        runButton = gr.Button("Generate")
    outVideo = gr.Video(label="Generated Video Output")
    outData = gr.Markdown()
    runButton.click(fn=generate, inputs=[prompt, seed], outputs=[outVideo, outData])

# Launch
webapp.queue().launch(server_port=7860, server_name="0.0.0.0")

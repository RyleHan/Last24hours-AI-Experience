# demo/test_image.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompts.prompt_generator import generate_prompt
from generator.image_gen import generate_image

if __name__ == "__main__":
    prompt = generate_prompt("我最爱的人", "月球基地", "Evanescence - My Immortal")
    print("🎯 Prompt:", prompt)

    generate_image(prompt, output_path="outputs/demo_img.png")
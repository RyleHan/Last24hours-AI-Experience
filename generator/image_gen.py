# generator/image_generator.py

import replicate
import os
from dotenv import load_dotenv

load_dotenv()
replicate_token = os.getenv("REPLICATE_API_TOKEN")
assert replicate_token, "请设置环境变量 REPLICATE_API_TOKEN"

replicate.Client(api_token=replicate_token)

def generate_image(prompt: str, output_path: str = "outputs/generated.png"):
    print("🚀 Generating image from prompt...")
    
    output = replicate.run(
        "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",
        input={
            "prompt": prompt,
            "width": 768,
            "height": 768
        }
    )

    # 🧠 处理返回格式
    if isinstance(output, list):
        output_url = output[0]
    elif hasattr(output, 'url'):
        output_url = output.url
    elif isinstance(output, str):
        output_url = output
    else:
        raise ValueError(f"❌ 无法解析的输出类型：{type(output)}")

    # ✅ 下载并保存图像
    import requests
    from PIL import Image
    from io import BytesIO

    image_data = requests.get(output_url).content
    image = Image.open(BytesIO(image_data))
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)

    print(f"✅ Image saved at: {output_path}")
# generator/caption_generator.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
assert api_key, "请设置环境变量 OPENAI_API_KEY"

client = OpenAI(api_key=api_key)

def generate_text(person: str, location: str, song: str) -> str:
    prompt = f"""
请用细腻、富有画面感的中文，描述一个“世界终结前24小时”的情感画面。设定如下：
- 和谁在一起：{person}
- 地点：{location}
- 听的歌：{song}

请生成一段类似“情绪海报”中的文案，情绪可以是温暖、悲伤或释然。
控制在 80~120 字。
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # 如果有 GPT-4 可以换成 gpt-4
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
    )

    return response.choices[0].message.content.strip()
# main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from prompts.prompt_generator import generate_prompt
from generator.image_gen import generate_image
from generator.text_gen import generate_text
from poster.create_poster import compose_poster

def ask_user_inputs():
    print("🧠 请回答以下问题，生成你的世界终结前 24 小时场景：")
    person = input("Q1️⃣ 你最想和谁在一起？\n👤：")
    location = input("Q2️⃣ 如果只剩 24 小时，你想待在哪里？\n📍：")
    song = input("Q3️⃣ 你会听哪首歌？（歌名+歌手）\n🎵：")
    weather = input("Q4️⃣ 最近天气怎么样？\n🌧️：")
    quote = input("Q5️⃣ 你最喜欢的一句话？\n📖：")
    return person, location, song, weather, quote

def main():
    person, location, song, weather, quote = ask_user_inputs()

    # 构建Prompt
    prompt = generate_prompt(person, location, song, weather, quote)

    # 生成图像
    generate_image(prompt, output_path="outputs/generated.png")

    # 生成文案
    caption = generate_text(person, location, song)

    # 合成海报
    compose_poster(
        background_path="outputs/generated.png",
        output_path="outputs/poster.jpg",
        caption=caption,
        person=person,
        location=location,
        song=song
    )

    print("\n✅ 你的情绪海报已生成：outputs/poster.jpg")
    print("✨ 用这张图感动面试官吧！")

if __name__ == "__main__":
    main()
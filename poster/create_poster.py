
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def compose_poster(
    background_path: str,
    output_path: str,
    caption: str,
    person: str,
    location: str,
    song: str
):
    # 加载图片
    image = Image.open(background_path).convert("RGBA")

    # 添加渐变模糊底部蒙版
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    for i in range(300):
        alpha = int(180 * (i / 300))
        draw_overlay.rectangle([(0, image.height - 300 + i), (image.width, image.height - 300 + i + 1)], fill=(0, 0, 0, alpha))
    image = Image.alpha_composite(image, overlay)

    # 创建可绘制对象
    draw = ImageDraw.Draw(image)

    # 设置字体
    font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"  # Mac字体路径
    font_caption = ImageFont.truetype(font_path, size=36)
    font_meta = ImageFont.truetype(font_path, size=24)

    # 绘制文案
    margin = 40
    caption_lines = wrap_text(caption, font_caption, image.width - 2 * margin)
    y_text = image.height - 260
    for line in caption_lines:
        draw.text((margin, y_text), line, font=font_caption, fill="white")
        y_text += 44

    # 绘制人物、地点、音乐
    meta_text = f"👤 {person}    📍 {location}    🎵 {song}"
    draw.text((margin, image.height - 60), meta_text, font=font_meta, fill="white")

    # 保存结果
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.convert("RGB").save(output_path)
    print(f"🎨 情绪海报生成成功：{output_path}")

def wrap_text(text, font, max_width):
    lines = []
    line = ""
    for char in text:
        if font.getlength(line + char) <= max_width:
            line += char
        else:
            lines.append(line)
            line = char
    lines.append(line)
    return lines
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generator.text_gen import generate_text

person = "妈妈"
location = "海边"
song = "朴树《那些花儿》"

caption = generate_text(person, location, song)

print("📝 海报文案：\n", caption)
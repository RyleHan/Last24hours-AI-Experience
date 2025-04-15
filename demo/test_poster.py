# demo/test_poster.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from poster.create_poster import compose_poster

caption = "我和妈妈坐在海边，听着朴树的《那些花儿》。世界明天就要终结了，但此刻海风温柔，我只想静静地靠着她。"
person = "妈妈"
location = "海边"
song = "朴树《那些花儿》"

compose_poster(
    background_path="outputs/demo_img.png",
    output_path="outputs/poster.jpg",
    caption=caption,
    person=person,
    location=location,
    song=song
)
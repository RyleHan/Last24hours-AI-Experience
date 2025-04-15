import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from prompts.prompt_generator import generate_prompt

prompt = generate_prompt("我的爱人", "冰岛的极光下", "理查德·克莱德曼的钢琴曲")
print(prompt)
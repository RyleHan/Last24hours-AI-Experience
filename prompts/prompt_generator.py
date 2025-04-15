# prompts/prompt_generator.py

def generate_prompt(person: str, place: str, music: str, weather: str, quote: str) -> str:
    """
    根据用户输入信息生成图像Prompt
    """
    mood_keywords = extract_mood_from_music(music)

    prompt = (
        f"In the last 24 hours before the end of the world, "
        f"{person} and you are in {place}. "
        f"The weather is {weather}, and a song like '{music}' is playing softly. "
        f"This moment is filled with deep emotion, as the words '{quote}' echo in your heart. "
        f"Visualize a cinematic, emotional scene with vivid colors, dramatic lighting, and a sense of calm before the end."
    )
    return prompt


def extract_mood_from_music(music: str) -> str:
    """
    简单的音乐关键词转情绪标签
    """
    music = music.lower()
    if any(keyword in music for keyword in ["悲伤", "伤感", "雨", "泪", "alone", "cold"]):
        return "sadness and solitude"
    elif any(keyword in music for keyword in ["希望", "梦", "love", "romantic"]):
        return "hope and love"
    elif any(keyword in music for keyword in ["末日", "毁灭", "rock", "战斗"]):
        return "chaos and fire"
    else:
        return "inner emotion"

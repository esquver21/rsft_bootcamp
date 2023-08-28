import random

def choice_from_range(text: str, start: int, finish: int) -> str:
    return random.choice(text[start:finish])
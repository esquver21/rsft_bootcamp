from others.symbols import is_vowel

def count_vowels(word: str) -> int:
    counter = 0
    for iterat in word:
        if is_vowel(iterat.lower()):
            counter += 1
    return counter
def is_vowel(symb: chr) -> bool:
    return symb.isalpha() and symb.lower() in 'aeiouаеёиоуыэюя'
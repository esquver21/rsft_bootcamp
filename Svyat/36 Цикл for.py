def filter_string(string: str, symbol: str) -> str:
    out = ""
    for char in string:
        if char.lower() != symbol.lower():
            out += char
    return out.strip()
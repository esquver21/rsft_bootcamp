def join_numbers_from_range(start: int, finish: int) -> str:
    rety = ""
    rety += "".join(str(iter) for iter in range(start, finish + 1))
    return rety
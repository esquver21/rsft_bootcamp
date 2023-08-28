def my_substr (string: str, lenght: int) -> str:
    ans = ""
    for iterator in range(lenght):
        ans += string[iterator]
    return ans
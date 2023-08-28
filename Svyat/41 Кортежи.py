def sort_pair(pair):
    one, two = pair

    if one > two:
        return (two, one)
    else:
        return pair
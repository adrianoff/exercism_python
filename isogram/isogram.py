def is_isogram(string: str):
    short = string.replace(' ', '').replace('-', '').lower()
    return len(short) == len(set(short))

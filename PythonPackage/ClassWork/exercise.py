def histogram(word: str) -> dict[str, int]:
    import string
    abc = string.ascii_lowercase
    map_ = {}
    for char in abc:
        map_[char] = word.lower().count(char)
    return map_


print(histogram("Alabama is  a town"))

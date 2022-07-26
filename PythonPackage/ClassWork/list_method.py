def cube(num: int) -> int:
    return num ** 3


cubes = [cube(i) for i in range(1, 11)]
print(cubes)

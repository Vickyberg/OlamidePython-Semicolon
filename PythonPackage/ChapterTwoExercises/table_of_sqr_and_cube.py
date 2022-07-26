print("{:<5}{:>8}{:>7}".format("Number", "Square", "Cube"))
square = 0
cube = 0
for num in range(0, 11):
    square = num * num
    cube = num * num * num
    print("{:<10}{:<10}{:<9}".format(num, square, cube))

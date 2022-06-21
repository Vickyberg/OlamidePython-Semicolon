import math
comparator = 100

num = int(input("Enter the number to compare: "))
num_square = math.pow(num,2)
if num > comparator:
    print(f"The number you entered is greater than {comparator}")
if num_square > comparator:
    print(f"The square of the number is greater than {comparator}")
if num < comparator:
    print(f"The number you entered is less than {comparator}")
if num_square < comparator:
    print(f"The square of the number is less than {comparator}")
if num == comparator:
    print(f"The number you entered is equal to {comparator}")
if num_square == comparator:
    print(f"The square of the number is equal to {comparator}")
if num != comparator:
    print(f"The number you entered is not equal to {comparator}")
if num_square != comparator:
    print(f"The square of the number  is not equal to {comparator}")
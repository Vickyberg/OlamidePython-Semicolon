import math

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
square_num1 = math.pow(num1, 2)
square_num2 = math.pow(num2, 2)
summation = square_num1 + square_num2
difference = square_num1 - square_num2
print("The square of the first number is:", square_num1)
print("The square of the second number is:", square_num2)
print("The sum of the squared numbers is :", summation)
print("The difference of the squared numbers is:", difference)

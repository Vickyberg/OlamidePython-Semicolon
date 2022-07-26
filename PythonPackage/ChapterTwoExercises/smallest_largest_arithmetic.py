num1 = int(input("Enter first positive integer:"))
num2 = int(input("Enter second positive integer:"))
num3 = int(input("Enter third positive integer:"))
print()
sum = num1 + num2 + num3
average = sum / 3
product = num1 * num2 * num3

print(f"The sum of {num1}, {num2} and {num3} is ", sum)
print(f"The average of {sum} is ", average)
print(f"The product of {num1}, {num2} and {num3} is ", product)
if num1 > num2 and num1 > num3:
    print("The largest number is ", num1)
if num2 > num3 and num2 > num1:
    print("The largest number is ", num2)
if num3 > num2 and num3 > num1:
    print("The largest number is ", num3)
if num1 < num2 and num1 < num3:
    print("The smallest number is ", num1)
if num2 < num3 and num2 < num1:
    print("The smallest number is ", num2)
if num3 < num2 and num3 < num1:
    print("The smallest number is ", num3)

user_input = input("Enter a five digits number: ")
if user_input.__len__() != 5:
    print("Not a five digits number")
else:
    for num in user_input:
        print(num, end='   ')

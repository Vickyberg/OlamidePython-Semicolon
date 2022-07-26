user_input = int(input("Enter a number: "))
for num in range(0, user_input):
    if 0 <= num <= user_input:
        print(num ** 2)

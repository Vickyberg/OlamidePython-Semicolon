lst = [i for i in range(1, 11)]
print(lst)
lst_2 = [i for i in range(1, 11) if i % 2 == 0]
print(lst_2)
x = "Even" if 4 % 2 == 0 else "Odd"
print(x)
lst_3 = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
print(lst_3)

lst_4 = [int(input(f"Enter student {i}'s score: ")) for i in range(1,6) ]
print(lst_4)
print("Total Scores = ", sum(lst_4))
print("Max = ",max(lst_4))
print("Min = ",min(lst_4))
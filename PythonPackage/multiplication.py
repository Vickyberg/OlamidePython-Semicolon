import itertools
name = "Ola"
lang = "Java"
age = 16

print("MULTIPLICATION TABLE")
for i in range(1,13):
    for j in range(1,13):
        print("{:<3} x {:3} = {:3}".format(i,j,i*j))
    print()

for i,j in itertools.product(range(1,13),range(1,13)):
    print("{:<3} x {:3} = {:3}".format(i, j, i * j))
    if j == 12:
        print()

fff = f"{name} is a {lang} lord and {name} is {age} years old"
print(fff)

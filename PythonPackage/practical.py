total = 0
_list = [2,5,6,7,9]
for x in _list:
    total = total + x
print(total)
key = 5
string = "Terminal"
string2 = "10110110"

print(string.lower())
print(string.upper())
print(string.title().split("m"))
print(string.capitalize())
print(string.rstrip())
print((string.find("m",1,3)))
print(string.index("a"))
print(string.isalpha())
print(string.endswith('l'))
print(string.startswith('T'))
print(string.removeprefix("Ter"))
print(string.swapcase())
print(string.count("l"))
print(string.__len__())
print(string.replace("m","o"))
print(string2.translate(string2.maketrans("10","01")))

river = "Mississippi"
target = input("Input a character to find: ")
for index,letter in enumerate(river):
    if letter == target:
        print("Letter found at index: ",index)
        break
else:
    print("Letter",target,"not found in",river)
print(f"{45:0^10d}")


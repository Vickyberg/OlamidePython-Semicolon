import string
abc = string.ascii_lowercase
user_input = input("Enter your word to cypher: ")
while not user_input.isalpha():
    user_input = input("Enter your word to cypher: ")
key = input("Enter your key: ")
if key.isdigit() < 26:
    key = int(key)
if user_input.isalpha():
    cipher = user_input.translate(str.maketrans(abc, abc[key:] + abc[:key]))
    print(cipher)
decipher = cipher.translate(str.maketrans(abc, abc[key:] + abc[:key]))
print(decipher)
# for i in range(5):
#     print({"10d --> 10d"})

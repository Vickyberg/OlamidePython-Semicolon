with open("hello.txt", mode="r", encoding= 'utf-8') as file:
    # file.write("I love writing\n")
    # file.write("I love reading\n")
    # file.writelines(['I am prone to violence\n', "I am Olamide\n"])
    # read = file.read()
    # print(read)
     for index, line in enumerate(file.readlines()):
        print(f"line {index + 1}: {line}")
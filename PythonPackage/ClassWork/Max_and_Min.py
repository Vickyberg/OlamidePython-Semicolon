lst = [11, 2, 44, 5, 2, 4, 5]
maximum_num = lst[0]
minimum_num = lst[0]
for n in lst:
    if n > maximum_num:
        maximum_num = n
        print(maximum_num)
for n in lst:
    if n < minimum_num:
        minimum_num = n
        print(minimum_num)

def avg(*numbers):
    from statistics import mean
    return mean(numbers)


print(avg(1, 2, 3, 4))

lst = [1, 2, 3, 4, 5]
# asterisks is used for packing and unpacking
print(avg(*lst))

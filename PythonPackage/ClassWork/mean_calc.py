def avg(*numbers):
    from statistics import mean
    return mean(numbers)


print(avg(1, 2, 3, 4))

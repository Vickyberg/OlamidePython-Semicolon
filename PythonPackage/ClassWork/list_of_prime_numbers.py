# for number in range(1, 101):
#     count = 0
#     for i in range(2, (number // 2 + 1)):
#         if number % i == 0:
#             count += 1
#             break
#
#     if count == 0 and number != 1:
#         print(" %d" % number, end='  ')


def is_prime(num: int) -> bool:
    import  math
    max_divisor = math.ceil(math.sqrt(num)) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False
    return True


print(is_prime(7))

primes = [i for i in range(1,101) if is_prime(i)]
print(primes)

# dictionary composition
primes_2 = {k:v for k,v in enumerate(range(1,10)) if is_prime(v)}
print(type(primes_2))
print(primes_2)
def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 1.8 + 32


fahrenheit = celsius_to_fahrenheit(100)
print(fahrenheit)


def get_digit(number, position):
    return print(number // (10 ** position) % 10)


get_digit(234, 1)
get_digit(5768,2)
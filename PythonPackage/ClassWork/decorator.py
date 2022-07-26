import time


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print("About to be decorated")
        value = func(*args, **kwargs)
        print("Just decorated")
        return value

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        time_taken = time.perf_counter() - start
        print(f"{func.__name__} took {time_taken:.2e}secs  to run")
        return val

    return wrapper


@print_decorator
def printer():
    return "I am a printer"


@print_decorator
@timer
def factorial(num: int) -> int:
    import math
    return math.factorial(num)


print(printer())
print(factorial(5))

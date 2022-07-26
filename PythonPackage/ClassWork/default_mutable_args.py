def appender(lst=None):
    if lst is None:
        lst = []
    lst.append("You")
    return lst


appender = ["You"]

print(appender)


def sub(a: int = 0, b: int = 0) -> int:
    return b - a


print(sub(b=10, a=15))
print(sub.__annotations__)

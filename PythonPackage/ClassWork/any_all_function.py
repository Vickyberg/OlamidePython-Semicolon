lst = [1, 2, 3, 4, 5, 8]
fun = all(True if i >= 7 else False for i in lst)
fun2 = any(True if i >= 7 else False for i in lst)
print(fun)
print(fun2)


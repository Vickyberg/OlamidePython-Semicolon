s1 = {1, 3, 5}
s2 = {1, 3, 5, 6, 3, 5, 5}
# s1.add(3)
# print(s1)
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)
print(s1 | s2)
print(s1.intersection(s2))
print(s1 & s2)
print(s2.issuperset(s1))

# dictionary
d1 = {'a': 1, 'b': 2, 'c': 3}
d1.update({'a': 5, 'g': 10})
print(list(d1.keys()))
print(type(d1.values()))
print(d1)

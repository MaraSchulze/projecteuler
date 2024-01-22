a = sum([x**2 for x in range(101)])
b = sum([x for x in range(101)])
b = b**2
print(a, b, b - a)
def func(x):
    lst = [i ** 3 for i in range(1, x)]
    return lst, x

a, b = func(5)

print(a); print(b)
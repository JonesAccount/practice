numbers = (4, 6, 2, "0", 12, 5)

lst = []
for n in numbers:
    if n % 2 == 0:
        lst.append(n)
tpl = tuple(lst)
for i in tpl:
    print(isinstance(i, int))

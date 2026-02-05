from random import randint as r

a = "Alex"
b = "Michael"
names = ["Bob", "Kate", "Paul"]
names.insert(r(0, len(names) - 1), a if len(a) > len(b) else b)
for i in names:
    print(i)
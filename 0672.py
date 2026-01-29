from random import randint as r
names = "Barbara jones SmIth SAM CaroL rubby"
print(names)
list = names.split(" ")
for i in range(len(list)):
    list[i] = list[i].capitalize()
print(", ".join(list))
a, b = (list[r(0, len(list) - 1)].upper()), (list[r(0, len(list) - 1)].lower())
print(a); print(b)
print(a.isupper())
print(b.isupper())
print(a.islower())
print(b.islower())
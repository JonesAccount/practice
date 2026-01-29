list = []

size = int(input("Size of list: "))
for i in range(size):
    list.append(input(str(i + 1) + ". "))
    list[i] = list[i].lower()
print(list)

for i in range(size):
    list[i] = list[i].capitalize()
print(list)

for i in range(size):
    list[i] = list[i].upper()
print(list)

for i in range(size):
    print(list[i].isupper())

for i in range(size):
    print(str(i + 1) + ". " + list[i])

for i in range(size):
    list[i] = list[i].islower()

print(list[2][:2:])
list = ["Gabriel", "Rick", "Ellie", "John", "Victor"]

for i in range(len(list)):
    list[i] = list[i].upper()

name2 = list[1]
name3 = list[2]
name1 = list[0]
print(name2[3::])
print(name3[4::])

print(list[0][2:-3], end="")
print(list[1][1].lower(), end="")
print(list[2][1:-2].lower())

print(list[1:-1])
print(list[::2])
print(list[0])
print(list[:-4])
print(list[:-4:])
print(list[1::2])
print(list[-3][2:])
print(list[::])
print(list[::-1])
print(list.reverse())
print(list.sort())
print(list[::-2])
print("GHost")
print(list)
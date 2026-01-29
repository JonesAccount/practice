words = "bublle jusie car ballon eath giant python"

list = words.split()
list.sort()
list.pop(3)
list.pop(-6)

list2 = []
size_list = len(list)
for i in list:
    list2.append(i.capitalize())
print(list2)

for i in range(len(list)):
    list[i] = list[i].capitalize()

print(list)

print(", ".join(list))
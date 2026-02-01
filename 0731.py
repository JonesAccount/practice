file = open("0730.txt", "r")

print(file.readline())
print(file.tell())

print(file.readlines())
print(file.tell())

file.seek(0)
print(file.read())

file.close()
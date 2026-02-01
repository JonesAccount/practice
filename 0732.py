file = open("0730.txt", "r", encoding="utf-8")

print(file.readline())

print(file.readlines(30))
file.seek(0)
print(file.tell())

print(file.read())

file.close()
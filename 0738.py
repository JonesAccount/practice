with open("0737.txt", "r", encoding="utf-8") as file:
    print(file.readline(), end="")
    position = file.tell()
    print(position)
    print(len(file.readlines()))
    file.seek(0)
    print(file.read())
    print(file.closed)

print(file.closed)

f = open("0737.txt", "r")
print(f.tell())
f.close()
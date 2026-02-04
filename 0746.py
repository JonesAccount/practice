with open("0745.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readlines())
    file.seek(0)
    print(file.read())
    print(file.tell())
    print(file.closed)
print(file.closed)
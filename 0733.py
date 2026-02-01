try:
    file = open('file.txt', "r", encoding="utf-8")
    f1 = file.readline()
    f2 = file.readline()
    print(f2 + f1)
    file.close()
except FileNotFoundError:
    print("File not found")
finally:
    print("Program ending...")
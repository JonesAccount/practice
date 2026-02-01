try:

    with open("0730.txt", "r", encoding="utf-8") as file:
        print(file.readline(), end="")
        print(file.readlines())

except FileNotFoundError:
    print("File not found")
finally:
    print("End.", file.closed)



filel = open("0730.txt", "r", encoding="utf-8")

print(filel.read(6))
print(filel.closed)

file = open("0728.txt", "r", encoding="utf-8")

l = file.readlines()
l.append("NEW")
print(l)
l.clear()
print(l)

file.seek(0)
print(file.read())

file.close()
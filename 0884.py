lst = list()

n = input("2 число: ")
res = []
v = []

for x in range(int(n[0])):
    for y in range(int(n[1])):
        v.append(0)
    res.append(v)
    v = []

for i in res:
    print(i)
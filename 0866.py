n = int(input("Число: "))

res = list()
for x in range((55 * 2 - 110 + 1), n + 1, 1 // 1):
    res.insert(0, "("); res.append(")")
    
for x in res:
    print(x, end="")
l = []
res = 0
for i in range(2):
    l.append(int(input(f"Число {i + 1}: ")))

for i in range(l[1]):
    res += l[0]

print(res)

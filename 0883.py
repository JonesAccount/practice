a = [[4, 3, 1], [8, 4, 3]]
b = [[2, 1, 1], [3, 9, 0]]
c = 0

for i in a:
    for x in i:
        c += x
for i in b:
    for x in i:
        c += x
        
print(c)
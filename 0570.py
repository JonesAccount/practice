l = [6, 4, -8, 2, -1, -9, 5]
print(l)

for i in range(len(l)):
    l[i - 1] = abs(l[i - 1])
    
print(l)

var = 0
for i in range(len(l)):
    var += l[i - 1]

var_r = var / len(l)
print(var_r)

for i in range(len(l)):
        if l[i] < var_r:
            l.pop(i)
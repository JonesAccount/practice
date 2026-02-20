from random import randint

N = [randint(-10, 10) for i in range(10)]

M = [
    "Четное" if i % 2 == 0 else "Не четное"
    for i in N
    if i >= 0
    ]
    
D = dict()

for i, v in enumerate(M):
    D[i] = f"{N[i]} – {v}"
    
for key, value in D.items():
    print(f" {key + 1}: {value}")
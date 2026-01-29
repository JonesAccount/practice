import random

l1 = []
l2 = []

def f(list):
    for i in range(10):
        list.append(random.randint(10, 30))
    return list

m1 = set(f(l1))
m2 = set(f(l2))

print(m1); print(m2, end="\n\n")
print("Пересичение:")
print(m1 & m2)
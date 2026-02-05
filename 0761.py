l1 = [3, 2, 8, 5, 9]
l2 = l1 + [5]
l3 = list(l1)
l4 = l1[:]
l5 = l1

print(l1)
print(l2)
print(l3)
print(l4)

print(id(l1))
print(id(l5))
print(id(l3))
print(id(l4))
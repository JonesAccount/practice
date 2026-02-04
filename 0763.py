from random import randint as r

l1 = list()
l2 = l1[:]

def generate(l):
    for i in range(3):
        l.insert(r(0, 2), r(0, 2))
    print(l)
    return l
    
generate(l1)
generate(l2)

print(l1 == l2)
print(l1 != l2)
print(l1 > l2)
print(l1 < l2)
print(l1 >= l2)
print(l1 <= l2)
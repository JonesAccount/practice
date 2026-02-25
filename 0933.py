A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

print(f"Original: {A}\n{B}\n")
A |= B
print(A)
print(A & B)
C = set()
for i in A:
    if i not in B:
        C.add(i)
print(C)
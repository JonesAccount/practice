from random import randint

A = [[randint(1, 9) for i in range(3)] for j in range(3)]

counter = 3
for i in A:
    print(i, end=""); counter -= 1
    print("  ", end="") if counter > 0 else None
print()

B = [[j[i] * j[i] for i in range(len(j))] for j in A]

counter = 3
for i in B:
    print(i, end=""); counter -= 1
    print("  ", end="") if counter > 0 else None
print("\n")

size = len(A)
for i in range(size):
    for j in range(size):
        print(f" {A[i][j]} = {B[i][j]}")
matrix = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
        ]
        
for i in matrix:
    for j in i:
        print(f" {j} ", end="")
    print()
    
matrix_lite = [
            [j + 1] * 3 for i in range(1)
            for j in range(3)
            ]
print()
for i in matrix_lite:
    for j in i:
        print(f" {j} ", end="")
    print()
t = {9, 36, 81, 144, 324, 441, 576, 729, 1089, 1296, 1521, 1764, 2304, 25, 100, 400, 625, 1225, 1600, 2500}
m = {i ** 2 for i in range(1, 50) if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0}

lst = sorted(list(m))

for i in range(len(lst)):
    print(lst[i], end=" ")
    
print(f"\n\n{t | m}")
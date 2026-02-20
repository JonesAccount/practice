tb = [
    f" {i} * {j} = {i * j}"
    for i in range(2, 10)
    for j in range(9)
    ]

counter = 0
for i in range(len(tb)):
    print(tb[i]); counter += 1
    if counter == 9:
        print(); counter = 0
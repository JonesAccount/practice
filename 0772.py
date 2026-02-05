n: int = int(input("Число: "))

counter = 0
for i in range(n):
    if i % 2 == 0:
        counter += 1
    if i % 3 == 0:
        counter += 1
    if i % 4 == 0:
        counter += 1
    if i % 5 == 0:
        counter += 1
    if i % 6 == 0:
        counter += 1
    if i % 7 == 0:
        counter += 1
    if i % 8 == 0:
        counter += 1
    if i % 9 == 0:
        counter += 1
    if counter < 2:
        print(i)
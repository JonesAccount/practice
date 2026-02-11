count = 3
while count > 1:
    n = int(input("::"))
    if n % 2 == 0:
        print(n)
    count -= 1
else:
    print(f"Итерация: {count}")
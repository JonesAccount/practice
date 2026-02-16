separator = "- " * 10
while True:
    n = input("Число: ")
    try:
        n = int(n)
        res = 1
        for x in range(1, n + 1):
            res *= x
        print(f"{n}! = {res}\n{separator}")
    except ValueError:
        try:
            n = float(n)
            print(f"Нельзя вещественное число!\n{separator}")
        except:
            if n.isalpha():
                print(f"Нельзя буквы!\n{separator}")
            elif n == "":
                print(f"Пусто!\n{separator}")
            else:
                print(f"Нельзя символы!\n{separator}")
num1 = int(input("Введи число: ")); num2 = int(input("Введи число: ")); num3 = int(input("Введи число: ")); num4 = int(input("Введи число: ")); num5 = int(input("Введи число: "))

chois = input("\n1 или 2: ")

if chois == "1":
    print("Результат:", min(num1, num2, num3, num4, num5))
elif chois == "2":
    print("Результат:", max(num1, num2, num3, num4, num5))
else:
    print("Ошибка ввода!")
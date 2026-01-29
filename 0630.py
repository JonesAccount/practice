try:
    num1, num2 = int(input()), int(input())
    res = num1 / num2
except ValueError:
    print("Введи число")
except ZeroDivisionError:
    print("На ноль нельзя")
else:
    print(res)
finally:
    print("прог завершена")
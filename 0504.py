num1, num2, num3 = int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: "))

def func():
    global num1, num2, num3
    num1 = abs(num1); num2 = abs(num2); num3 = abs(num3)
    if num1 % 2 != 0:
        num1 += 1
    if num2 % 2 != 0:
        num2 += 1
    if num3 % 2 != 0:
        num3 += 1
    
func()

print()
print(num1, num2, num3, sep="|")
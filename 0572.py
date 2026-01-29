num = int(input("Введи число: "))

if num % 3 == 0 and num % 5 == 0:
    print(str(num) + " делится на 3 и 5")
elif num % 3 == 0 or num % 5 == 0:
    print(str(num) + " делится на одно число")
else:
    print(str(num) + " не делится ни на что")
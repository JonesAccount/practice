from random import choice as c, randint as r

this_let = None
password = ""
numbers = "1234567890"
simvols = "@#$_&-+()/*\"\':;!?~`|=[]%{}"
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

print("ГЕНЕРАЦИЯ ПАРОЛЯ\n")

size = input("• Длина пароля: ")
    
while True:
    can_num = input("• Включать цифры? да/нет: ")
    if can_num == "да" or can_num == "нет":
        break
    else:
        continue
while True:
    can_let = input("• Включать буквы? да/нет: ")
    if can_let== "да" or can_let == "нет":
        break
    else:
        continue
while True:
    can_sim = input("• Включать символы? да/нет: ")
    if can_sim == "да" or can_sim == "нет":
        break
    else:
        continue

for i in range(int(size)):
    this_let = r(1, 4)
    if this_let == 1 and can_let == "да":
        password += c(letters)
    elif this_let == 3 and can_sim == "да":
        password += c(simvols)
    elif can_num == "да":
        password += c(numbers)

print("\nПароль создан: ", end=""); print(password)
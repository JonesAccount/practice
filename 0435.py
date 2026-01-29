line = "——————————————————————————————"
print("• КАЛЬКУЛЯТОР 3.0 •", end="\n\n"); print(line)

print("-ОПЕРАНДЫ-")
num_one_check = input("|Первое число| >>> ")
num_two_check = ""

number_one = 0
number_two = 0

if num_one_check >= 1 or num_one_check <= 1:
    if number_two >= 1 or number_two <= 1:
        number_two = input("|Второе число| >>> ")
    else:
        print("Неверный операнд!")
else:
    print("Неверный операнд!")
    

print("\n-ОПЕРАТОРЫ-")
print("|+", "-", "*", "/| >>> ", sep="|", end="")
operation = input()
print(line, end="\n\n")

if operation == "+":
    print("Результат: " + str(number_one) + " + " + str(number_two) + " = " + str(number_one + number_two))
elif operation == "-":
    print("-")
elif operation == "*":
    print("ghj")
elif operation == "/":
    print("jguj")
else:
    print("Неверный оператор!")
    
#  не рабочий код
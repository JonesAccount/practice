word = input("Введите слово: ")
print(str(word) + "\n")

choice = int(input("Выберите: \n1. Метод upper\n2. Метод lower\n3. Метод capitalize\n"))

if choice == 1:
    print("\nРезультат: " + word.upper())
elif choice == 2:
    print("\nРезультат: " + word.lower())
elif choice == 3:
    print("\nРезультат: " + word.capitalize())
else:
    print("Неправильный ввод")
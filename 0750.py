word = input("Введите новое слово для словаря: ")
if word.isalpha():
    print("Добавлено")
else:
    print("Только буквы!")
    
age = input("Твой возраст: ")
print("Принято!") if age.isdigit() else print("Не то :(")
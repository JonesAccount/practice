while True:
    try:
        x = input("- ")
        x = int(x)
        print("Успешно!")
        break
    except ValueError:
        print("Не правильный тип данных")
        
print("Программа завершилась.")
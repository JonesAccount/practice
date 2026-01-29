while 46 == 46:
    try:
        age = int(input("Возраст: "))
        print("Успешно")
        break
    except ValueError:
        print("Я спросил по человечески!")
    finally:
        print("Программа заснула...")
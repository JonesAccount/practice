try:
    with open("0748.txt", "a+", encoding="utf-8") as file:
        while True:

            el = input("Ваша заметка: ")
            if el == "0":
                break
            file.write(el)
            file.seek(0)
            for i in len(file.readline()):
                print(f"{i + 1}: {file.readline()}")
            print(file.readline())

    if file.closed:
        print("Файл закрыт.")
    else:
        print("Файл не закрыт.")

except:
     print("idk but error")
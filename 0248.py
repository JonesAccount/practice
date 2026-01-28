word = "cake"
print("Слово: " + word)
letter = input("Выбрано буква: ")
print(letter + "\n")

if letter == "c":
    count = word.find("c")
    print("Индекс буквы " + letter + ": " + str(count))
elif letter == "a":
    count = word.find("a")
    print("Индекс буквы " + letter + ": " + str(count))
elif letter == "k":
    count = word.find("k")
    print("Индекс буквы " + letter + ": " + str(count))
elif letter == "e":
    count = word.find("e")
    print("Индекс буквы " + letter + ": " + str(count))
else:
    print("Ошибка ввода")
from random import choice, randint

# Переменные
alphabet: str = "йцукенгшщзхфывапролджэячсмитьбю"
alphabet_red: str = "еыаоэяь"
text: str = ""
word: str = ""
line: str = "·" * 25
    
# Генератов слова
for size in range(2, 10 + 1):
    
    # Первая буква слова
    while True:
        word += choice(alphabet)
        if "ь" not in word:
            break
        else:
            word = ""
            
    # Остальные буквы слова
    size_word = randint(2, 10)
    while not False:
        if len(word) == size_word:
            break
        else:
            choice_letter = choice(alphabet)
            if word[-1] in alphabet_red:
                if choice_letter not in alphabet_red:
                    if word[-1].lower() != choice_letter:
                        word += choice_letter
            else:
                if choice_letter in alphabet_red:
                    if word[-1].lower() != choice_letter:
                        word += choice_letter
                    
    # Добавление в текст
    text += f" {word}"
    word = ""

# Делаем первую букву заглавной
cap = text[1].upper()
text = " " + cap + text[2:]

# Показываем в консоли
print(line)
counter: int = 0
for sym in text:
    if sym == " ":
        counter += 1
    if counter == 3:
        print(",")
        counter = 0
    print(sym, end="")
print(".")
print(line)
latin_letters = [
    "a", "b", "v", "g", "d",
    "e", "yo", "zh", "z", "i",
    "y", "k", "l", "m", "n",
    "o", "p", "r", "s", "t",
    "u", "f", "kh", "ts", "ch",
    "sh", "shch", "", "y", "",
    "e", "yu", "ya"
]

cyrillic_letters = [
    "а", "б", "в", "г", "д",
    "е", "ё", "ж", "з", "и",
    "й", "к", "л", "м", "н",
    "о", "п", "р", "с", "т",
    "у", "ф", "х", "ц", "ч",
    "ш", "щ", "ъ", "ы", "ь",
    "э", "ю", "я"
]

word = input("Предложение: ")
word = list(word.lower())

for i, v in enumerate(cyrillic_letters):
    if v in word:
        word[word.index(v)] = latin_letters[i]
        
word = "".join(word)
print(word)
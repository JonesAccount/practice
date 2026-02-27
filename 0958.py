words = [
    "шалаш",
    "уровень",
    "радар",
    "дом",
    "заказ",
    "казак",
    "потоп",
    "привет",
    "дед",
    "мама",
    "noon",
    "civic",
    "apple",
    "rotor",
    "world",
    "kayak",
    "refer",
    "python",
    "madam",
    "code"
]


def palid(word) -> bool:
    """
    Проверяет, является ли строка палиндромом
    """
    if word == word[::-1]:
        return True
    else:
        return False
    
res = {word: palid(word) for word in words}
    
for key, value in res.items():
    print(f"{key}: {value}")
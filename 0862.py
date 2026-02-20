d = {
    "car": "машина",
    "stone": "камень",
    "house": "дом",
    "cat": "кошка"
        }
        
user_key = input("Ключ: ")

try:
    print(d[user_key.lower()].capitalize())
except KeyError:
    print("Такого ключа нет.")
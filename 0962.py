db = [
    "Alice",
    "bob",
    "Alice",
    "BOB",
    "alice99",
    "Charlie_",
    "alice",
    "Charlie",
    "bob007",
    "DAVID",
    "alice123",
    "Charlie_42",
    "Bob",
]

user_input = input(" Ник: ")

if user_input not in db:
    if len(user_input) >= 3:
        if user_input[0].isdigit():
            print(" Нельзя начать с цифр.")
        elif not user_input[0].isalpha():
            print(" Нельзя начать с символа.")
        else:
            print(" Ник принят")
            db.insert(0, user_input)
    else:
        print(" Минимальная длина 3")
else:
    print(" Ник занят")
    
print(f" {db[0]}")
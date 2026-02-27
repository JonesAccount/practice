import pickledb
import os

card = 0

def update_console():
    click = input("Нажмите enter")
    os.system('cls' if os.name == 'nt' else 'clear')


def balance():
    print(f"\nВаш баланс: {db.get('card')}")
    update_console()


def send(sum = 0) -> str:
    """
    Внести средсва на карту
    """
    global card
    card += sum
    db.set('card', card)
    print(card)


def take() -> str:
    """
    Снять средва с карты
    """
    global card
    if card >= sum:
        card == sum
    else:
        print("Недостаточно средтсв")


while True:
    print("\nВаша карта\n\n[1] - баланс\n[2] - пополнить\n[3] - снять")
    try:
        action = int(input("Операция: "))
        if 0 < action < 4:
            if action == 1:
                balance()
        else:
            print("Неправильный запрос")
    except ValueError:
        print("Неправильный запрос")

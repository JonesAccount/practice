def calories(cola, fanta):
    c = cola * 42
    f = fanta * 46
    return c, f

drink_cola = int(input())
drink_fanta = int(input())

c, f = calories(drink_cola, drink_fanta)
print("В " + str(drink_cola) + " литре колы = " + str(c) + " калорий")
print("В " + str(drink_fanta) + " литре фанты = " + str(f) + " калорий")
print("\nОбщее количество калорий: " + str(c + f))
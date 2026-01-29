from time import sleep as s

time = 0
while True:
    try:
         time = int(input("Таймер. Пиши до 20 секунд: "))
         if time > 0 and time < 21:
             break
    except ValueError:
        print("Нужно ввести число.")
    finally:
        print(f"Принято: {time}", end="\n\n")

for i in range(time):
    s(1)
    print(f"Время: {i + 1}")
    
print("\n!ЗВОН!")
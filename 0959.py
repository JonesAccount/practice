from random import randint
from time import sleep
import os


def season(n = 8) -> str:
    while 1:
        if n == 1 or n == 2 or n == 12:
            print(f"Месяц {n} –> зима")
        elif 3 < n < 6:
            print(f"Месяц {n} –> весна")
        elif 6 < n < 9:
            print(f"Месяц {n} –> лета")
        elif 9 < n < 12:
            print(f"Месяц {n} –> осень")
        n = randint(1, 12)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


season()

# зима: 1, 2, 12
# весна: 3, 4, 5
# лета: 6, 7, 8
# осень: 9, 10, 11

if name == 'main':
    main()
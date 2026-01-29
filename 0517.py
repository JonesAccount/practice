num = int(input("Число: "))

def f1(): # проверка на четность
    global num
    f2() if num % 2 == 0 else print("#1 не прошло!")
    
def f2(): # проверка на величину #1
    global num
    f3() if num > 6 else print("#2 не прошло!")

def f3(): # проверка на величину #2
    global num
    print("Число что есть!") if num < 30 else print("#3 не прошло!")

f1()
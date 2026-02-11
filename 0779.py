from time import sleep

def start_program():
    print("Простой таймер")
    time = int(input("Засекать время на: "))
    return time
    
seconds = start_program()

def timer():
    global seconds
    while seconds >= 0:
        print(f"\rОсталось: {seconds}", "сек.  " if seconds < 10 else "сек.", end="", flush=True)
        sleep(1)
        seconds -= 1

timer()

print("\n\nВремя вышло")
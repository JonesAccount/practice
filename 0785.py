def counter(step: int = 0):
    def start():
        nonlocal step
        step += 1
        print(step)
    start()
    return start
    
f1 = counter()
f2 = counter()
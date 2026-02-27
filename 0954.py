from time import time


def counter(n=99999999) -> int:
    """
    Скорость выполнения операции.
    """
    start = time()
    while n != 0:
        n -= 1
    end = time()
    
    print(f"{round(end - start)}")


counter()
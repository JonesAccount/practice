def recursion(counter: int = 1) -> str:
    print(f"Глубина рекурсии – {counter}")
    try:
        recursion(counter + 1)
    except RecursionError:
        print("Максимальная глубина")


counter = 1
def cycle() -> str:
    global counter
    if counter != 2:
        recursion()
    counter += 1
    

cycle()
order = (
        "Иван",
        ("Ноутбук", 80000),
        ("Мышь", 1500),
        ("Коврик", 500)
        )

decoder = dict(
            discount=10,
            delivery=300
            )
            

def fuck(client, *args, **kwargs) -> str:
    print(f"Клиент: {client}")
    
    lst = []
    for i in range(1, len(args)):
        lst.append(args[i])
        
    summa = 0
    for tupl in lst:
        print("- ", end="")
        check = True
        for el in tupl:
            print(f"{el}", ": " if check else "", sep="", end="")
            check = False
            if isinstance(el, int):
                summa += el
        print(" руб.")
        
    print(f"Сумма: {summa} руб.")
    print(f"Скидка {kwargs["discount"]}%: -{int(summa - (summa - (summa * 0.1)))} руб.")
    print(f"Доставка: {kwargs["delivery"]} руб.")
    print(f"Итого: {int(summa - (summa * 0.1) + kwargs["delivery"])} руб.")
    

fuck(order[0], *order, **decoder)
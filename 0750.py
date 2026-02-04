with open("0748.txt", "a+") as f:
    while True:
        el = input("Write: ")
        if el == "0":
            break
        f.write(el + "\n")
    lst = f.readlines()
    f.seek(0)
    for el in range(len(lst)):
        print(lst[el])
from random import randint

list = []

while True:
    list.extend([randint(1, 5), randint(1, 5), randint(1, 5)])
    if list[0] == list[1] and list[0] == list[2]:
        print(list)
        break
    else:
        list.clear()
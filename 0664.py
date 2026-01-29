from random import choice, randint

list = []
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"

for i in range(randint(10, 30)):
    for i in choice(letters):
        list.append(i)

print(list)

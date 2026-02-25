word = "дед мороз старый пердун"
lst = [i for i in "аеёиоуыэюя"]

g, s = 0, 0

for i in word:
    if i.isalpha():
        if i in lst:
            g += 1
        else:
            s += 1
print(g, s)
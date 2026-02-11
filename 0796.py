word = input("Строка: ")

d = {}

if word.isalpha():
    if " " not in word:
        for i in word:
            d[i] = word.count(i)
        print(d)
    else:
        print(False)
else:
    print(False)
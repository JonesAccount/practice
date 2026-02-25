word = "abracadabra"

lst = []

for i in word:
    n = word.count(i)
    if n == 1:
        lst.append(i)
        
print(lst[0] if len(lst) > 0 else "Уникальных нет")
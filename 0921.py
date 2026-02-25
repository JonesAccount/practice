word = "abracadabra"

lst = []

for i in word:
    n = word.count(i)
    if n == 1:
        lst.append(i)
        
print(lst[0] if word.index(lst[0]) < word.index(lst[1]) else lst[1])
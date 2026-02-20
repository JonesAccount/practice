word = "прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон Хьюстон у нас проблема"

lst = [i for i in word.split()]

print(f"\n {word}")

pro = []
for i in range(len(lst)):
    el = lst[i]
    pro.append(el)
    print(f" {pro.count(el)}", end="")

print("\n 1 1 2 1 1 2 1 2 3 1 3 1 1 1")
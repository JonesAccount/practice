words = "Если хочешь, могу потом дать ещё более сложную версию, где:"

m = set(words)
l = list(m)
l = sorted(l)

for i in l:
    if i.isalpha():
        print(i.lower())
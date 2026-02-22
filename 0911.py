lst = ["Banana", "2", "Apple", "4.3", "Qiwi", "Strayberry"]
array = [w for w in lst if w.isalpha()]
fruits = [fr for fr in array if len(fr) > 5]
size_fr = dict()
for name in fruits:
    size_fr[name] = len(name)


for key, value in size_fr.items():
    print(f"{key}: {value}")
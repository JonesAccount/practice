lst = [[2, "неудовлетворительно"], [3, "удовлетворительно"], [4, "хорошо"], [5, "отлично"]]

d = dict()

for main in lst:
    for i in main:
        d[main[0]] = main[1]
        
for key, value in d.items():
    print(f"{key}: {value}")
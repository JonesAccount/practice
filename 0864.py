lst = [[2, "неудовлетворительно"], [3, "удовлетворительно"], [4, "хорошо"], [5, "отлично"]]

d = dict(lst)
        
for key, value in d.items():
    print(f"{key}: {value}")
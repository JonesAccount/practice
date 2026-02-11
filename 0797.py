string = "Напиши функцию на Python, которая принимает строку и возвращает самый часто встречающийся символ в этой строке. Если таких символов несколько — верни тот, который встречается первым."

string = string.replace(" ", "")

d = dict()

for i in string:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

counter: int = 1
for k, v in d.items():
    print(f"{counter}: {k} – {v}")
    counter += 1
    
key = None
value = 0
for k, v in d.items():
    if v > value:
        value = v
        key = k
        
print(f"\nСамый частый символ: {key} – {value}")
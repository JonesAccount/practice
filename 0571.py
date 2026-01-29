d = { 
    "name": {
        "n1": "Daniel",
        "n2": "Samanta",
        "n3": "Frank",
        "n4": "Bell"
            },
    "age": {
        "a1": 12,
        "a2": 19,
        "a3": 17,
        "a4": 20
            }
        }
    
for values in d["age"].values():
    if values >= 18:
        print(values)

num_age = 0
for values in d["age"].values():
    num_age += values
num_age = num_age // len(d["age"])
print()
print(num_age)

d["age"].popitem()
print(d)

for i in d["name"].items():
    print(i)
for i in d["age"].items():
    print(i)
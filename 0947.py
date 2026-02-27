m = {i: "четное" if i % 2 == 0 else "нечетное" for i in range(1, 20)}
m2 = {i: i  2 if i % 2 == 0 else i  3 for i in m.keys()}

for k, v in m.items():
    print(k, v)

print()

for k, v in m2.items():
    print(k, v)
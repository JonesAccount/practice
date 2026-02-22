lst = ["1", "2", "3", "4", "5"]
d = dict.fromkeys(lst, "NULL")
print(d)
d2 = d.copy()
d2["2"] = True
print(d2)
d3 = dict(d2)
d3["5"] = False
print(d3)

print(d2.get("8", "Not the key"))

print(d.setdefault("11"))
del d["11"]
print(d)
i = d.pop("40", not False)
print(d)
print(i)
d.popitem()
print(d)
v = d.keys(); values = d2.values(); c = d3.items()
print(v); print(values); print(c)

for k, v in d3.items():
    print(k, v)

d5 = dict.fromkeys(lst, None)
d5["2"] = True; d5["3"] = "Good"; d5["5"] = 100

d6 = dict.fromkeys(lst, None)
d6.pop("2"); d6.pop("5")
d6["city"] = "Detroit"
d6["88"] = 35.4
print(d5); print(d6)
d5.update(d6)
print(d5)

d7 = {d2, d3}
print(d7)

l = [1, 2 ,3]
u = dict.fromkeys(l, "nothing")
u["4"] = "nothing"
u2 = dict.fromkeys(l, "something")
u3 = u | u2
print(u3)
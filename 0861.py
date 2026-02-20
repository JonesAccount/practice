d = {}

d[(1, 2)] = True
d[frozenset(d)] = False
d["Boat"] = not False

print(d)
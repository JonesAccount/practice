set1 = {"C", "B", "M"}

set1.add("L")
print(set1)

set2 = {"A", "M", "E"}
sets = set1.difference(set2)
print(sets)

set1.union(set2)
print(set1)

set1.remove("C")
print(set1)

set1.clear()
print(set1)
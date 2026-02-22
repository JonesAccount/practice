data = (10, "Hello", [1, 2, 3], 3.14, "Python")

counter = 0
for i in data:
    print(f"{i}: {type(i)}")
    if isinstance(i, str):
        counter += 1
print(f"str in the data: {counter}")

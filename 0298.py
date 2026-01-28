set_string = {"Python", "C++", "Java"}

set_int = {100, 34, 67}

set_float = {66.6, 2.0, 23.50}

set_bool = {True, False, None}

sets = set_string.union(set_int, set_float, set_bool)

for i in sets:
    print(i)

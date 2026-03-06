word = "PythonScript"

it = iter(word)

while True:
    try:
        print(next(it), end="")
    except:
        break
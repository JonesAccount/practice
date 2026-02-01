try:
    with open('0730.txt', 'r', encoding="utf-8") as f:
        print(f.read(2))
        for i in f:
            print(f.readline())
except FileNotFoundError:
    print("File not found")
from time import sleep

a, b = 43, 27
while True:
    big = a if a > b else b
    small = b if b > a else a
    d = big % small
    if d == 0:
        print(f"Done! {d}")
        break
    print("...")
    sleep(0.5)
from time import sleep
import sys

print("Welcome to program")
def func():
    st = 0
    while 1:
        st += 1
        print(f"\rCounter: {st}", end="")
        sleep(1)
print("Bye!")
func()
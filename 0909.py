from time import sleep; import sys

print("=== TOP LINE ===")
print("Counter: 0")
print("=== BOTTOM LINE ===")

st = 0
while 1:
    st += 1
    sys.stdout.write(f"\033[F")
    sys.stdout.write(f"Counter: {st}\n")
    sys.stdout.flush()
    sleep(1)
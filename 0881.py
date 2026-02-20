nums = [3, 7, 2, 9, 4]

it = iter(nums)

for x in range(len(nums)):
    num = next(it)
    if num % 2 != 0:
        print(f" {num}")
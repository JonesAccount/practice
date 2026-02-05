numbers = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

l = list()

l.extend(numbers[0]); l.extend(numbers[1]); l.extend(numbers[-1])

print(sum(l))
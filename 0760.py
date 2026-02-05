numbers = [[3, 1, 4], [2, 8], [5, 7, 6]]
print(f"Исходник:\n{numbers}")
numbers = numbers[0] + numbers[1] + numbers[2]
print(f"Обьединяем:\n{numbers}")
print(f"По возрастанию:\n{sorted(numbers)}")
print(f"По убиванию:\n{sorted(numbers, reverse=True)}")
print(f"Сумма всех чисел:\n{sum(numbers)}")
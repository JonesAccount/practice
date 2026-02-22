from random import randint

students = ["Bob", "Stive", "James", "Tom"]
grades = {}
for s in students:
    grades[s] = randint(2, 5)
best = [v for k, v in grades.items() if v > 3]
for i in best:
    print(i)
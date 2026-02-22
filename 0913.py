students = {
    "Анна": 85,
    "Иван": 78,
    "Мария": 92
}

print(students.get("Аннамария"), "Студент не найден")
students.setdefault("Олег", 70)
print(students["Олег"])
students.setdefault("Иван", 50)
print(students["Иван"])
s = {"Светлана": 88, "Дмитрий": 81}
s.update(students)
print(s)
print(students.popitem())
del students["Иван"]
print(students)
cop = students.copy()
for k, v in cop.items():
    cop[k] = v + 1
print(cop)

subjects = ["Математика", "Физика", "История"]
subject = dict()
subject = subject.fromkeys(subjects, 0)
print(subject)

c = (4, 7, 6, 9)
d = dict()
d = d.fromkeys(c, None)
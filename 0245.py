hour = int(input("Сколько часов в день работал: "))
print(hour, "\n")
day = int(input("Сколько дней работал: "))
print(day)

hour_cash = 1000
day_cash = 9000

result_hour = hour_cash * hour
result_day = day_cash * day

print("\nОплата за часы: " + str(result_hour) + "\nОплата за дней: " + str(result_day))

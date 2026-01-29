try:
    num = int(input())
    res = num * num
except ValueError:
    print("ошибся!")
else:
    print(res)
finally:
    print("коннц..")
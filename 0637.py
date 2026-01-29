class Lst:
    def f(self, x, y):
        print(x); print(y)
        x = set(x); y = set(y)
        per = x & y
        li = tuple(per)
        listi = []
        for i in range(len(li)):
            listi.append(li[i])
        
        print(listi)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

l = Lst()
l.f(a, b)
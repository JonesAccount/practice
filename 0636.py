class Xi:
    def listin(self, list1, list2):
        print(list1)
        for i in range(len(list1)):
            if list1[i] > 5:
                list2.append(list1[i])
        print(list2)
        
    
    
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

x = Xi()
x.listin(a, b)
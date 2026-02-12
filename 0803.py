text1 = "Привет мир, как твои дела?"
text2 = "Мир большой, привет всем!"

# → уникальные слова первого текста: ['дела', 'как', 'твои']

m = {}

l = ["!", "?", ",", ".", "  "]

def dfunc(D):
    global l
    for el in l:
        D = D.replace(el, " ").lower()
    return D
    
text1 = dfunc(text1); text2 = dfunc(text2)

def sfunc(S):
    return S.strip()
    
l1 = sfunc(text1).split(" ")
l2 = sfunc(text2).split(" ")

reslist = list()

for el in l1:
    if el not in l2:
        reslist.append(el)
        
reslist.sort()
print(reslist)
word = ["Python", "java", "FoRtran", "C#"]
word = " ".join(word); print(word)

word = ["Python", "java", "FoRtran", "C#"]
res = ""
for el in range(len(word)):
    res += word[el]
    res += " "
    
print(res)
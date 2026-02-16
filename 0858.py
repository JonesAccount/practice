digs = [4, 34, -12, 8, 94]

for i, v in enumerate(digs):
    if len(str(v)) > 1:
        digs[i] = 0
    
print(digs)
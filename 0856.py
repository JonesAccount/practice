digs = [4, 34, -12, 8, 94]

for n in range(len(digs)):
    if len(str(digs[n])) > 1:
        digs[n] = 0
        
print(digs)
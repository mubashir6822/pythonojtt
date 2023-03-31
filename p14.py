l = [1,None,None,3,None,4]
for i in range(len(l)):
    for x in l:
        if not x:
            x[i]=x[i-1]
print(l)
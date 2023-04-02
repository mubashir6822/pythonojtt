def float_range(start,stop,step):
    l=[]
    while start<stop:
        l.append(start)
        start+=step
    return l
    

r=float_range(0.5,2.5,0.5)
print(list(r))

print(len(r))

for n in r:
    print(n)
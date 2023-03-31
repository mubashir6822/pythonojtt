a = [8,9,10,"f",5,8,"d"]
l=[]
for x in a:
    if (type(x)==int):
        i=x*x
        l.append(i)
    else:
        s=x+x
        l.append(s)
a=l
print(a)

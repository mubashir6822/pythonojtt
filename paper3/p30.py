test_list=[2323,82,129388,95]
d={}
for x in test_list:
    x=str(x)
    h=len(x)//2
    print(h)
    d[int(x[:h])]=int(x[h:])
print(d)
with open('f.txt','r')as f1:
    data=f1.read().split()
a=0
for x in data:
    if x.isdecimal()==True:
        a+=int(x)
print(a)
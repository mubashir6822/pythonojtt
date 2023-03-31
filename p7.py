s = "adfw$vf&yvy*ugv%uy"
x=''
l=[]
for i in range(len(s)):
    if s[i].isalnum():
        x=x+s[i]
    else:
        l.append(s[i])
        l.append(i)
        
x=list(x[::-1])
for i in range(0,len(l),2):
    x.insert(l[i+1],l[i])

print(s)
print(''.join(x))
print(l)
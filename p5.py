l1=[2,3,4,5,6,7,8,9,10]
l2=[]

for i in l1:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l2.append(i*i)
print(l2) 
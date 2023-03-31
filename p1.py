l1=[2,1,4,3,5,7,6]
for i in range(len(l1)): 
    for j in range(i + 1, len(l1)): 
        if l1[i] > l1[j]: 
           l1[i], l1[j] = l1[j], l1[i] 
sec_higest_num=l1[-2]
print('second highest number is : ',sec_higest_num)
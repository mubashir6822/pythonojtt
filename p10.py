lst = [56,2,13,1,78,4,6]
for i in range(len(lst)): 
    for j in range(i + 1, len(lst)): 
        if lst[i] > lst[j]: 
           lst[i], lst[j] = lst[j], lst[i] 
dec_ord_sort=lst[::-1]
print('decending order sort : ',dec_ord_sort)
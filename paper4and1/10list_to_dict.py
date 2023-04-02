from functools import reduce 
l1=["emp1","emp2","emp3"]
l2=[1,2]
crate_dict=dict(zip(l1,l2))
print("dictinory by using 2 lists ",crate_dict)

print("sum of values are : ",sum(crate_dict.values()))

summ=reduce(lambda x,y:x+y,crate_dict.values())

print("reduce ->",summ)
l1=[1,2,3]
l2=['a','b','c']

def interleave(l1,l2):
    l3=[]
    if len(l1)==len(l2):
        for i in range(len(l1)) :
            l3.append(l1[i])
            l3.append(l2[i])
        return l3
    else:
        return 'not valid'

print(interleave(l1,l2))


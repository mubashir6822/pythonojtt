l1=[1,2,3,4]
l2=[5,6,7,8]
def combinelist(l1,l2):
    l=l1+l2
    return l

print(combinelist(l1,l2))

def comblist(l1,l2):
    for x in l2:
        l1.append(x)
        n=l1
    return n

print(comblist(l1,l2))
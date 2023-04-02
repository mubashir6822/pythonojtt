l=[1,2,3,4]

def half_split(l):
    z=len(l)//2
    return (l[:z],l[z:])
print(half_split(l))

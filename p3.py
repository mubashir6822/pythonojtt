l=[2,3,4,5,6,7,8,8]
index=int(input())
# l.pop(int(index))
# print(l)
l=l[:index]+l[index+1:]
print(l)
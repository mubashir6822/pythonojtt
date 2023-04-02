# def uniq(l):
#     uniqlist=[]
#     for x in l:
#         if x not in uniqlist: 
#             uniqlist.append(x)
#     print(uniqlist)

# l=[1,1,1,2,3,4,5,6,6]
# uniq(l)
# l=[2,3,4,5,6,6,6,7,7]
# uniq(l)
def uniq(l):
    l=list(set(l))
    return l

print(uniq([1,1,2,2,3,4,5]))
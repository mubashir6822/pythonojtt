# l=[2,3,-5,-7,9,4,6,-2,-8,0]
l=[2,1]
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)
print(sorted(l))
x=l.sort()
print(l)

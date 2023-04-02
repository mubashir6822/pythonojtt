def genn(n):
    for i in range(n):
        if i%5==0 and i%2==0 and i!=0:
            yield i

g=genn(int(input("enter value : ")))
for i in g:
    print(i,end=" ")

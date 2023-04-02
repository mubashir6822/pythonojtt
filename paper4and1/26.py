n=int(input("enter number : "))
x=''
for i in range (1,n+1):
    x+=str(i)
    if i%2==0:
        print(x[::-1]+'*')
    else:
        print('*'+x) 
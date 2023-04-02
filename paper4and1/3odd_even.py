num=[4,5,7,2,9,8]
even=[]
odd=[]
for x in num:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
dictnory={"even":even,"odd":odd}
print(dictnory)
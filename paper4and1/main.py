import add_sub
from div_mul import division,multiplication

v1= int(input('enter val1 : '))
v2= int(input('enter val2 : '))
op=input()
if op=='+':
    add_sub.addition(v1,v2)
elif op=='-':
    add_sub.subtraction(v1,v2)
elif op=='*':
    multiplication(v1,v2)
elif op=="/":
    division(v1,v2)
else:
    ('give proper input')
    
# only upto 2 decimal point
# print("addition of v1 and v2 = ",addition(v1,v2))
# print("substration of v1 and v2 = ",subtraction(v1,v2))
# print("multiplication of v1 and v2 = ",multiplication(v1,v2))
# print("division of v1 and v2 = ",division(v1,v2))

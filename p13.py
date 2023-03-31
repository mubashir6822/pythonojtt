try:
    input1=int(input())
    input2=int(input())
    if type(input1)==int and type(input2)==int:
        if input1>input2:
            print(input1/input2)
        else:
            print(input2/input1)
except ZeroDivisionError:
    if input1==0 or input2==0:
        print("can't divide by zero")
except ValueError:
        print('input should be an integer')


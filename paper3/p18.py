class WrongnumberError(Exception):
    'Check lenght of phone number'
    pass
input_num=input('enter your number :')

try:
    if len(input_num) == 10:
        print('valid number :',input_num)
    else :
        raise WrongnumberError

except WrongnumberError:
    print('invalid number : you enterd a wrong number')
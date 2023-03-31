def credit_card(num):
    if len(num)==16:
        return (('*'*14)+num[-4:])
    else:
         return 'check num once'
print(credit_card('1234748393999900'))

'''Rewrite the program to get proper output'''

match = 'version'
input=8
#print(Match+input) ---> give type error
print(match+str(input))



# -------------------------------------



import math
import schedule
def pat():
    print('****')
schedule.every(2).seconds.do(pat)

while True:
    schedule.run_pending()
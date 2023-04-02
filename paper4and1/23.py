import time

starttime=time.time()
def lst(l):
    for x in range (l):
        print("running")
lst(22) 
stoptime=time.time()
print("time taken for exicuting program is : ",stoptime-starttime)

# count of time in sec or min
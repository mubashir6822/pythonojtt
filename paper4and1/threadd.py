from threading import * 
class thrd:
    def m(self):
        l=[1.1,2,4,'mubashir']
        for x in l:
            print("chaild ->",x)
y=thrd()
t1=Thread(target=y.m)
t1.start()
t1.join()
print("completed....",current_thread())

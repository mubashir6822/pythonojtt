'''Q14 : When do you use generators in python? Give an example'''

''' In Python, a generator is a function that returns an iterator that 
produces a sequence of values when iterated over'''

import sys
def genn(n):
    for i in range(n):
        yield i
print(genn)
g=genn(7)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)
# print(sys.getsizeof(g))
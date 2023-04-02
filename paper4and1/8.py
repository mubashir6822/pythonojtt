# program to find sum of multiple numbers 

'''This function takes any number of positional arguments and returns a string obtained by concatenating 
all the input arguments together. The return type of this function is a string.
However, if we define a different function that takes arbitrary positional arguments and
 performs a different operation, the return type could be different'''

def names(*args):
    
    print(args)
    print(type(args))

names("mubashir","mudassir")

def kw(**kwargs):
    print(kwargs)
    print(type(kwargs))
kw(a="mubashir",b=2,c=2)

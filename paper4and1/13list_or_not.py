
def lst(l):
    if type(l)==list:
        print("valid argument")
    else:
        print("invalid aargument")

lst([1,2,3,"mubashir"])
lst((1,2,3,4))

print("======================")

def lst(l):
    if isinstance(l,list):
        print("valid argument")
    else:
        print("invalid aargument")

lst([1,2,3,"mubashir"])
lst((1,2,3,4))
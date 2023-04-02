def add(x,y):
    try:
        print("sum of two integer is :", x+y)
    except TypeError:
        print("cannot not concanetate string and integer")
add(2,4)
add("a",6)





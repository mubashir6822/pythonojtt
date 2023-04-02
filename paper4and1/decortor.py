'''A decorator is a design pattern in Python that allows a user to add new functionality 
to an existing object without modifying its structure.'''

def uppercase_decorator(function):
    def wrapper():
        func1 = function()
        make_uppercase = func1.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper
    
# say_hi=uppercase_decorator(say_hi)
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())


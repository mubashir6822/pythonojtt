def recod_calls(func):
    def wrapper(x,y):
        wrapper.call_count+=1
        return f'the adition of given num is {func(x,y)}'
    wrapper.call_count=0
    return wrapper

@recod_calls
def add(x,y):
    return x+y

print(add(4,5))
print(add(5,6))
print(add(9,6))
print('number of call_count is : ',add.call_count)


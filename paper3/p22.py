def is_iterator(x):
    try:
        if next(x):
            return True
    except:
        return False

print(is_iterator(iter([1,2,3,4,5])))
print(is_iterator([1]))
print(type(iter([])))

print('-------------------------------------')

def is_iterator2(l):
    if hasattr(l,'__iter__') and hasattr(l,'__next__'):
        return True
    else:
        return False

print(is_iterator2(iter([])))


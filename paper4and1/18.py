a=[1,3,4,5]

try:
    print(a[4])
    # print(float(a))
    # print(int('a'))
    # print(a.upper())
except IndexError:
    print("out of range")
except TypeError:
    print("check given type")
except ValueError:
    print("check value")
except AttributeError:
    print("check your attribute")
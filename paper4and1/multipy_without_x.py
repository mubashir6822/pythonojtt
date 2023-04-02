'''16. Write a program to multiply two given number without using “*” operation and any in built
function'''

# def multiply(a, b):
#     result = 0
#     for i in range(b):
#         result += a
#     return result


r=(lambda a,b: a/(1/b))

print(int(r(2,4))) #2+2+2+2
print(int(r(8,4))) #8+8+8+8

# try with lambda
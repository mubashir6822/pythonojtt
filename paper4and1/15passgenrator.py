import random
import string
length = int(input('enter the length of password: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
pass_gen = random.sample(all,length)
password = "".join(pass_gen)
print("password genrated successfully => ",password)

# try using fuction
print(ord('0'))
print(ord('9'))

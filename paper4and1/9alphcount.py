
input_str = input("enter string : ")
output_str = ""

for i in range(len(input_str)):
    output_str += input_str[i] + str(i+1)

print(output_str)

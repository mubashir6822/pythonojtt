input_str=input()

char_count = {}


for char in input_str:
   
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Create a new string with each alphabet and its count
output_str = ''
for char in input_str:
    if char.isalpha():
        output_str += char + str(char_count[char])
    else:
        output_str += char

print(output_str)

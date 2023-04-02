l=[1,2,3,2,4,2,4,7,8,4,5,8,6,9,2]

even_key={}

for num in l:
    if num%2==0:
        if num in even_key:
            even_key[num]+=1
        else:
            even_key[num]=1
print(even_key)


# -----------------------------------------

input_list = [2, 3, 5, 6, 6, 6, 8, 8, 10]

even_dict = {}

for num in input_list:
    if num % 2 == 0:
        even_dict[num] = even_dict.get(num,0) + 1

print(even_dict)
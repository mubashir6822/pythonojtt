str_list =["anna", "amma", "apple","pen","pop" ]

pallindrome_str=[]
for x in str_list:
    if x == x[::-1]:
        pallindrome_str.append(x)
print(pallindrome_str)


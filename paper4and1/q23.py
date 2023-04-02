'''Find the highest sum of the string by removing the duplicates 
input=1211 '''

str_list = input()
int_list = []
for num in str_list:
    int_list.append(int(num))
print(int_list)
unique_list =set(int_list)
s=sum(unique_list)
print(s)


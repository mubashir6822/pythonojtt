my_dict = {'apple': 3, 'orange': 2, 'banana': 1}

print(my_dict.items())
print(sorted(my_dict.keys()))
print(sorted(my_dict.values()))

print(sorted(my_dict.items()))

# sort by keys and print key-value pairs
for key in sorted(my_dict):
    print('sort by keys ->' ,key, my_dict[key])

print('----------------------')
# sort by values and print key-value pairs
for key,value in sorted(my_dict.items(), key=lambda val: val[1]):
    print('sort by values ->' ,key,value)


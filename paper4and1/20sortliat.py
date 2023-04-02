def get_last_character(string):
    #return the last character of a string.
    return string[-1]

names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

sorted_list = sorted(names_list, key=get_last_character)

print(sorted_list)

# ---------------------------------------------

# names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']

# sorted_list = sorted(names_list, key=lambda x: x[-1])

# print(sorted_list)

import re

given="Msys&Technologies@Chennai0987389"

w_spl_chr = re.sub("[^a-z A-Z]", " ", given)

print(w_spl_chr)


# special_string="Msys&Technologies@Chennai"

# special_characters=['@','#','$','*','&']
# normal_string=special_string
# for i in special_characters:

#     normal_string=normal_string.replace(i," ")

# print("string after conversion:",normal_string)

sentence = ("I need to work very hard to learn more about algorithms in Python!")

w=sentence.split(' ')
w_l=len(w)
s=''.join(chr for chr in sentence if chr.isalnum())
print('total length of word :',len(s) )

# l=(sentence.replace(" ",""))
# z=l.replace("!","")
# print(z)
print('average length of word is :',len(s)//w_l)
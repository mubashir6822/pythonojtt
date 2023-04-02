lst = [10, 20, 30,40, 50, 60]

def swap_element(lst,p1, p2):
    lst[p1], lst[p2] = lst[p2], lst[p1]

swap_element(lst, 2, 0)
print(lst)

# print('-----------------------------------')

# def swap_3elements(lst1, p1, p2, p3):
#     lst1[p1], lst1[p2], lst1[p3] = lst1[p3], lst1[p1], lst1[p2]


# lst1 = [1, 2, 3, 4, 5]

# swap_3elements(lst1, 0, 2, 4)
# print(lst1)  

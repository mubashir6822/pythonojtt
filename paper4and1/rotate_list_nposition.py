def right_rotate_list(lst, n):
    return lst[-n:] + lst[:-n]

lst = [1, 2, 3, 4, 5,6,7]
n = int(input("Enter index position to rotate list item: "))
rotated_lst = right_rotate_list(lst, n)
print(rotated_lst)








#indexing
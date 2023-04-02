def rotate(l, n):
    return l[-n:] + l[:-n]


# def rotate(l, n):
#     return l[n:] + l[:n]


example_list =  [10, 20, 30, 40, 50, 60, 70]

print(rotate(example_list, 3))










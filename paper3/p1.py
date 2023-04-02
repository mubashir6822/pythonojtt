def substr(s1,s2):
    for c in s1:
        if c in s2:
            return 'Yes'
    return 'No'
        
print(substr('hi','by'))
print(substr('yes','no'))
print(substr('good','food'))
print(substr('mubashir', 'mudasir'))
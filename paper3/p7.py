
def anagraam(a,b):
    if sorted(a)==sorted(b):
        return True
    else:
        return False
    
print(anagraam(input(),input()))
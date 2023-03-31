def last_line(f):
    with open(f, "r") as f1:
        last = f1.read().splitlines() 
        last=last[::-1] 
    return last

for line in last_line('t.txt'):
    print(line)

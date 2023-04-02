def post_range(s):
    s=s.split(',')
    l=[]
    for x in s:
        start,end=x.split('-')
        # print(start,end)
        for num in range(int(start),int(end)+1):
            l.append(num)

        
    
    print(l)
post_range('1-2,3-4,5-8')
class Row:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)


r=Row(a=10,b=20)
print(r.a)
print(r.b)
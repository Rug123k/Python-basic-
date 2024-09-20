def maths():
    a,b=12,34
    def add():
        print("*"*10)
        c=a+b
        print(c)
        print("*"*10)
    return add
m=maths()
m()
        
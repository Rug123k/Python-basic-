# variable length positional Arguments

# 1) variable length Arguments

def fun(*args):
    print(type(args),args)
fun()
fun(12,11,22)

def fun1(a,b,*args):
    print(type(args),a,b,args)
# fun1()
fun1(12,11,22)
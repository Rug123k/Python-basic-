# also we can write the last program in try and except block

def div(a,b):
    if b !=0:
        c= a//b
        return c
    else:
        raise ZeroDivisionError
a=int(input("Enter first number"))
b=int(input("Enter second number"))

try:
    c=div(a,b)
    print(c)
except:
    print(ZeroDivisionError)
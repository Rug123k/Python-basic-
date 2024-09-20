# Decorator Function
# passing function as a parameter
# Nested function calling funcation
# return nested function

def decorator(fun):
    def wrapper():
        print("*"*10)
        fun()
        print("*"*10)
    return wrapper

def display():
    print("Hello")

d=decorator(display)
d()
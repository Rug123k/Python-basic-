g=10
def fun1():
    global g
    g=g+4
    print(g)
fun1()
print("global",g)

# we canot modify global varible without defining global
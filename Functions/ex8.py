# unpacking arguments
def fun(a,b,c):
    print(a, b, c)
L1=[11,22,33]

fun(L1[0], L1[1], L1[2])

fun(*L1)
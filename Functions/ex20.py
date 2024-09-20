# Sum of scores Ending with zero
def sum(L):
    s = 0
    
    for e in L:
        if e%10==0:
            s=s+e
    return s
L=[100,125,200,234,300] #for e in l meanse a number which will store in the list(l)
print(sum(L))
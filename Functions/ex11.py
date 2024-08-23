# Generators
def Days():
    L=['sun', 'mon', 'tue', 'wes', 'thu', 'fri', 'sat']
    i=0
    while True:
        x=L[i]
        i=(i+1)%7
        yield x
        
d=Days()
print(next(d))
print(next(d))
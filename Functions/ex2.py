# positional Argument
def net_sal(basic,allowance,tax):
    net=basic+allowance-tax
    return net
n=net_sal(78000,16000,11000)
print("This is sal" ,n)
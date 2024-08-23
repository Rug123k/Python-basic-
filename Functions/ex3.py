# Keyword Arguments
def net_sal(basic,allowance,tax):
    net=basic+allowance-tax
    return net
n=net_sal(allowance=16000,tax=11000,basic=78000)
print("This is sal" ,n)
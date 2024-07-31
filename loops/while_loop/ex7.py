# Revarsing the number

n=12359
rev=0

while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
    
    
    # 12359>0,
    # r=n%10  r=123459%10  =9
    # rev(0)=(rev)0*10+(r)9
    # n=1235
    
    # 1235>0
    # r=n%10  r=1235%10  =5
    #rev=rev*10+r    9*10+5 =95
    #n=123
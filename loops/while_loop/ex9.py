# convert a decimal num to binary num


# how to convert a num
# n=11
#             Num
# 2|11
# 2|5         - "1"      2*2*2*2*2=10  so we will select the 5 and 2*5 is 10 so we substract 11-10 = we get  
# 2|2         - "1"
# 2|1         - "0"
#             - "1"           read the Num from down to top so YOu will get the binary number for 11

n=int(input("Enter a number to convert binary"))
bin=0

while n>0:
    r=n%2
    n=n//2
    bin=bin*10+r
rev=0
while bin>0:
    r=bin%10
    bin=bin//10
    rev=rev*10+r
print(rev)

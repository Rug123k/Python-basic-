# Find A sum of digits in a number
n=12359
count=0
sum=0

while n>0:
    r=n%10
    n=n//10
    sum=sum+r
print("sum =",sum)



# n =12359  , while = 12359>0  true  , r(variable)=12359% 10 =9 ,0=0+9 sum=9 , n=12359//10 n=1235  this steps can repeat

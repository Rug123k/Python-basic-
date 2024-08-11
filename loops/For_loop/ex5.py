# Find out fac of given number

n=int(input("Enter a number"))
count=1
fact=1
for count in range(1,n+1):
    fact=fact*count
print(fact)
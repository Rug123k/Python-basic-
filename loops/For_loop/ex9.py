n=int(input("Enter a number"))
count=0

for i in range(1,n+1):
    if n%i==0:
        count+=1                        # in this block it will cheack how many time n % i == 0 and increase the count if the count is more then 2 time the it is not prime

if count ==2:
    print("Prime number")       #it wil check how many time count will run
else:
    print("Not prime")


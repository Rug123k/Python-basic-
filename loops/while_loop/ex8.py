# Find max number from given numbers

num=int(input("Enter a number"))      #this code will tell how many num of num you want to enter
max=0
count=0

while count<num:
    n=int(input("enter a number"))
    if n>max:
        max=n
    count+=1
print("max value is ", max)



# n= 2 1 5 7
# count(0)<num(4), 2>0 true ,max = 2 ,count1
# count(1)<num(4) ,1>2 false,max = 2, count2
# count(2)<num(4) ,5>2 true,max = 5, count3
# count(3)<num(4) ,7>5 true,max = 7, count4

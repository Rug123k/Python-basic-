# counting the number of digit in number

# we will take help of flow division  
# ex 20//3 ==6  ----- in flow div we will not write a numbers after  point


n=12359
count=0

while n>0:
    n=n//10
    count+=1
print("num of digit",count)
    
    
# count is use to tell how many time loop run and from that we can find the total num of digit

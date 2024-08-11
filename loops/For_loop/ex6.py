# print a term of ap series

a=int(input("Enter inital term"))
b=int(input("Diff"))
n=int(input("num of terms"))

for t in range(a,a+n*b,b):
    print(t)
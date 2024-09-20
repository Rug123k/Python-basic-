# handling to error in one exception
l=[10,20,30,40,50]
try:
    index=int(input("Enter index"))
    print(l[index])
    print("end of try block")
except(IndexError,ValueError) as msg:
    print(msg)
print("terminated")
L= [10,20,30,40,50]

try:
    index=int(input("Enter index"))
    print(L[index])
    print("End of try block")
except IndexError:
    print("invalid index")
except ValueError:
    print("Enter only integer")
    
print("Terminated")
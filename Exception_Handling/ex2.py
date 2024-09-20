L= [10, 20, 30, 40, 50]

try:
    index=int(input("Enter index"))
    print(L[index])
except:
    print("Invalid index")
print("terminated gracefully")
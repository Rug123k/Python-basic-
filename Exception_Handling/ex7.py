print("Before try")

try:
    a =int(input("Enter Num"))
    b=int(input("enter num"))
    c=a//b
except ZeroDivisionError as error:
    print(error)
else:
    print("div is", c)
print("outside try except")
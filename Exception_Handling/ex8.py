print("Before try")

try:
    a =int(input("Enter Num"))
    b=int(input("enter num"))
    c=a//b
except ZeroDivisionError as error:
    print(error)
else:
    print("div is", c)
finally:
    print("finally block")         #this block alsays run if erroe come or not this block always run
print("outside try except")
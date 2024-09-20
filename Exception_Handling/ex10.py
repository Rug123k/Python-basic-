# Nested try except
try:
    a=int(input("Enter a first number"))
    try:
        b=int(input("Enter second number"))
        try:
            c=a/b
        except ZeroDivisionError as e:
            print(e)
    except ValueError:
        print("value error")
    
except ValueError:
    print("value error")
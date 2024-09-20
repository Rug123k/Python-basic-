# challenge account balance
class Account(Exception):
    pass
bal=10000

def withdraw(amt):
    global bal
    
    if bal- amt<5000:
        raise Account("min bal 5000")
    else:
        bal=bal-amt
        print("remaining bal is", bal)
try:
    withdraw(6000)
except Account as e:
    print(e)
# Guess the number Between 1-10

import random
guess=0
n=random.randint(1,10)           #it will selct the automatioc number between 1 to 10

while guess != n:
    guess=int(input("guess num"))
    
    if guess<n:
        print("it is smaller")
    elif guess>n:
        print("it is larger")
    else:
        print("Coreect Guess")
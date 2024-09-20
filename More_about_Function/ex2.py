def closure(msg):
       # msg="hello"
       # print("hi")
        def display():
                 print("*"*10)
                 print(msg)
                 print("*"*10)
        return display

d=closure("hello bro")
d()
# global variable and local variable

g=10                              #Global variable
 
def fun1(a,b):                    #local variable(a,b,c)
      c=a+b                       #global variable can be acces in the fun but local variable canot acces in out of function
      print(g)
      print(c)
      
fun1(2,4)

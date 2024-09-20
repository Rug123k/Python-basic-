# Static Method
# this method not access class method and instance method
class Rectangle:
    count =0
    
    def __init__(self,length,Breadth):
        self.length=length
        self.breadth=Breadth
        
    
    def parameter(self):
        return 2*(self.length +self.breadth)
    
    def area(self):
        return self.length*self.breadth
    @staticmethod                          #it will not use the parameter from class it will take diffrent parameter out side class
    def issquare(len,bre):          
        return len==bre

 
r1=Rectangle(10,12)
print(Rectangle.issquare(10,12))

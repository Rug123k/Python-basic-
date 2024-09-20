# by using class variable in to out of class
class Rectangle:
    count =0
    
    def __init__(self,length,Breadth):
        self.length=length
        self.breadth=Breadth
        Rectangle.count+=1
    
    def parameter(self):
        return 2*(self.length +self.breadth)
    
    def area(self):
        return self.length*self.breadth
    
r1=Rectangle(10,12)
print(Rectangle.count)
        
        
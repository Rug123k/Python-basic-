# this is a type of method is wriiten in class
#Accessors (get) = use full for reading the proprty of a class an a obj
# Mutators (set) = use for writ and updating class an is obj

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def geLength(self):
        return self.length
    def setLength(self,l):
        self.length=l
    
    def parameter(self):
        return 2*(self.length +self.breadth)
    
    def area(self):
        return self.length*self.breadth
  
r =Rectangle(10,5)
print(r.geLength())
print(r.area())
r.setLength(15)
print(r.area())
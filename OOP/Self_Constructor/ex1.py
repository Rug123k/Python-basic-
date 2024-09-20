# def__init__ -- This is Constructor Method
# Whin you create obj of class automaticly that function(constructor is called)
# if you dont write a constructor ther is default constructor is present in python

# Self is refrance for current obj

class Cuboid:
    def __init__(self,l,b,h):
        print(id(self))
        self.length  = l
        self.breadth = b
        self.height  = h
    
    def lidarea(self):
        return self.length *self.breadth
    def total(self):
        return 2*(self.length *self.breadth + self.breadth*self.height +self.length* self.breadth)
    def volume(self):
        print(id(self))
        return self.length*self.breadth*self.height
c1 = Cuboid(12,8,4)
print(id(c1))
c1.volume()
print(c1.volume())
c2 = Cuboid(22,42,2)
print(id(c2))
c2.volume()
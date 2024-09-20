# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

class Cuboid:
    def __init__(self,l,b,h):
        self.length  = l
        self.breadth = b
        self.height  = h
    
    def lidarea(self):
        return self.length *self.breadth
    def total(self):
        return 2*(self.length *self.breadth + self.breadth*self.height +self.length* self.breadth)
    def volume(self):
        return self.length*self.breadth*self.height
c1 = Cuboid(12,8,4)
print(c1.volume())
print(c1.total())
print(c1.lidarea())




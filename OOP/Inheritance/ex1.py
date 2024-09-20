#                                        parent class
#                                            |
#                                            |
#                                            |
#                                            |
#                                            |
#                                         Child class 
# # A Python program to demonstrate inheritance


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def parameter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth


class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        super().__init__(l, b) # calling parent class without super class chaild class never take value from parent class
        
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.height


# Example usage:
r = Cuboid(10, 5, 4)
print(r.area())       # From Rectangle class
print(r.parameter())  # From Rectangle class
print(r.volume())     # From Cuboid class

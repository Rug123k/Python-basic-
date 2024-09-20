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
    @classmethod                                #we will create a count method inside the class
    def countReact(cls):
        print(cls.count)
r1=Rectangle(10,12)
r2=Rectangle(12,34)
Rectangle.countReact()
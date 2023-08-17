#it allows different objects to respond to same methods in their own way

class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.142*self.radius **2
class Square:
    def __init__(self,side):
        self.side= side
    def area(self):
        return self.side **2

#creating object
shape=[ Circle(5),Square(4)]
for i in shape:
    print("Area is: ",i.area())
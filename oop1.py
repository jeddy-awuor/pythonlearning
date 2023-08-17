class Circle:
    def __init__(self,radius):
        self.radius=radius

    def CircleArea(self):
        return 3.142*self.radius**2

    #alt
    #print(

circle=Circle(5)
print("My area is: ",circle.CircleArea())


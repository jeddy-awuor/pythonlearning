#class is blueprint for creating object.
#objects are instance of classs.
class Students:
    #defining method
    def __init__(self,name,gender,age):
    #creating variables
        self.name=name
        self.gender=gender
        self.age=age
   #creating function for method
    def sayhello(self):
        print("My name is",self.name, ". I am",self.gender, "and i am",self.age,"years old.")

#creating an object
myobj=Students("Jeddy", "Female", 20)
myobj.sayhello()

myobj=Students("Awuor", "Female", 19)
myobj.sayhello()
class Animal:
    def __init__(self,name):
        self.name= name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "barks"
class Cat(Animal):
    def speak(self):
        return "meows"

mydog=Dog("Fur")
mycat=Cat("Fluffy")

print(mycat.speak())
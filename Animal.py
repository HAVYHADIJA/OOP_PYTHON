class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("The Animal is speaking")

class Dog(Animal):
    def speak(self):
        print("The dog is barks")
class Cat(Animal):
    def speak(self):
        print("The Cat Meows")

Animal =[Dog(),Cat()]
for a in Animal:
    a.speak()

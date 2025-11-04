class Animal:
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


class Shape:
    def calculate_area(self):
        print("This is the area of the shape is 0")
class Rectangle(Shape):
    def __init__(self,):
        super().__init__()
    def calculate_area(self):
        print()

class Circle(Shape):
    def calculate_area(self):
        print()

Shape =[Rectangle(),Circle()]
for S in Shape:
    S.calculate_area()



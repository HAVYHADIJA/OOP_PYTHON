class Person:
    def __init__(self,name):
        self.name = name

# Method to introduce the person
    def introduce(self):
        return f"Hi, my name is {self.name}."

person1 = Person("Haddy")

print (person1.name)
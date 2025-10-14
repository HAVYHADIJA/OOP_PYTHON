class Person:
    def __init__(self,name):
        self.name = name

# Method to introduce the person
    def introduce(self):
        return f"Hi, my name is {self.name}."

person1 = Person("Haddy")

print (person1.name)

class Student(Person):
    pass

class Lecturer(Person):
    pass
    
p = Person("Boaz")
s = Student("Steve")
l = Lecturer("Theo")

print(p.introduce())
print(s.introduce())
print(l.introduce())
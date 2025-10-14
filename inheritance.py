class Person:
    def __init__(self,name):
        self.name = name

# Method to introduce the person
    def introduce(self):
        return f"Hi, my name is {self.name}."

person1 = Person("Haddy")

print (person1.name)

class Student(Person):
    def __init__(self, name, program, year):
        super().__init__(name)
        self.program = program
        self.year = year

class Lecturer(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    
p = Person("Boaz")
s = Student("Steve")
l = Lecturer("Theo")

print(p.introduce())
print(s.introduce())
print(l.introduce())
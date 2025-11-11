class Student:
    def greet(self):
        print("Hi,I'm a student.")
class ClassRep(Student):
    def greet(self):
        print("Hello, I'm the Class Rep, I am taking attendence!")

class GuildPresident(Student):
    def greet(self):
        print("I'm the Guild President- let's improve campus")

people =[Student(),ClassRep(), GuildPresident()]
for p in people:                    #same call different outputs
    p.greet()
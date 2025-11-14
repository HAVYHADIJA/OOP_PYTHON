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

#Abstraction is hiding internal complexity. we only code simple methods
#Abstract class(blueprint) help to design contracts or rules
#Abstract methods, (with no code inside)

from abc import ABC, abstractmethod #Helps us make an abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Vehicle(ABC):
    @abstractmethod
    def display_info(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def displayInfo(self):
        pass
        
class Car(Vehicle):
    def __init__(self,num_doors):
        self.num_doors = num_doors
        super().__init__()

    def display_Info(self):
        print(f"This car has,{self.num_doors}doors")

Car1 = Car(7)


    
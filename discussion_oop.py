class Car: #key word class starts with small c but the class car starts with capital c
    def __init__(self, name,color,Year):
        self.name=name
        self.color=color
        self.Year=Year
    def drive(self):
        print(f"I love driving,{self.name}")
    
name1= Car("BMW", "RED", "2022")
name1.drive()

class Girl:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dances(self):
        print(f"{self.name} knows how to dance.")
girl1 = Girl("Havy",20)
girl1.dances()

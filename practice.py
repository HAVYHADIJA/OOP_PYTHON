class Car:
    def __call__(self, brand, year):
        self.brand = brand
        self.year = year

    def honk(self):
        return f"My {self.brand} says Beep Beep!"
    
# Create an instance of the class and use it outside the class definition
Car1 = Car()
Car1("BMW", 2020)

print(Car1.honk())

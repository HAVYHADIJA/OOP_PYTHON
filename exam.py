"""patient = "John Smith"
age = 20
is_new = True

age = input("John,How old are you? ")
print(f"You are {age} years old.")

birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year
print(age)


course = 'Python for Beginners'
print(course.upper())
print(course)

course.lower()
print(course.lower())

print(course.replace('Beginners', 'Absolute Beginners'))

#IF Statements
temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("Its a nice day")
elif temperature > 10:
    print("Its a cold day")
else:
    print("Its cold")

#while loops
i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

i = 100
while i >= 1:
    print(i)
    i= i - 1

# Lists
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[-1])
print(names[2:4])
names[0] = 'Jon'
print(names)

numbers = [1, 2, 3, 4, 5]
print(len(numbers))

numbers = [1,2,3,4,5,6]
for item in numbers:
    print(item)"""




class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def stay(self):
        print(f"{self.name} stays in {self.house}")

student1 = Student("Martha"," Kololo Flats")
student1.stay()

class Person:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def drives(self):
        print(f"{self.name} drives a {self.car}")

person1 = Person("Richard", "Range Rover")
person1.drives()

class Shape:
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides
    def describe(self):
        print(f"This shape is {self.color} and has {self.sides} sides.")
shape_a = Shape("Blue", 3)
shape_b = Shape("Red", 4)
shape_c = Shape("Green", 5)
shape_a.describe()
shape_c.describe()


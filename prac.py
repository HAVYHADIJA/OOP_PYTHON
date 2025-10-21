class Student:
    def __init__(self,name,age,):
        self.name = name
        self.age = age

    def getStudent(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"{self.title} by {self.author}, {self.year}")

book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("Atomic Habits", "James Clear", 2018)
book3 = Book("Database Systems: A Practical Approach to Design, Implementation,and Management", "Connoly and Begg", 1995)

book1.describe()
book2.describe()
book3.describe()

class Hostel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def mention(self):
        print(f"{self.name} stays at {self.location}")

hostel1 = Hostel("havy", "Sabiiti")
print(hostel1.mention())



random_str = "aaa"
print(random_str.upper())

hostel2 = Hostel("Merinah","ST.MICHEAL")
print(hostel2.mention())


        
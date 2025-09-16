class Car:
    def __init__(self,brand,year):
       self.brand = brand
       self.year = year


#class book
class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        def describe(self):
            print(f"{self.title} by {self.author}, {self.year}")

book1 = Book("To Kill a Mockingbird","Harper Lee",1960)
book2 = Book("Atomic Habits","James Clear",2018)
book3 = Book("Database Systems: A Practical Approach to Design, Implementation,and Management","Connoly and Begg",1995)

print(book1.describe())
print(book2.describe()) 
print(book3.describe())

#MY MINI PROJECT ASSIGNMENT

    



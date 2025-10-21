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
class Hostel:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.visits = []   # list to keep visits

    
#Method to record a visit
    def record_visit(self, visitor, resident):
        # save visitor name + ID, and resident name
        self.visits.append((visitor.name, visitor.IDno, resident.name))
        print(f"Visit recorded: {visitor.name} (ID: {visitor.IDno}) visited {resident.name}")

        # Method to show all visits
    def show_visits(self):
        print(f"\nVisits at {self.name}:")
        if not self.visits:
            print("No visits yet.")
        else:
            for i, (visitor_name, visitor_id, resident_name) in enumerate(self.visits, start=1):
                print(f"{i}. {visitor_name} (ID: {visitor_id}) visited {resident_name}")
class Resident:
    def __init__(self,name,room): 
        self.name = name
        self.roomNumber = room
class visitor:
    def __init__(self,name,IDno):
      self.name = name
      self.IDno = IDno

hostel = Hostel("David's Ark Hostel", "Ankrah hill")

resident1 = Resident("Gabriella", "C3")
resident2 = Resident("Atu", "A14")

visitor1 = visitor("Havy", "B2123")
visitor2 = visitor("Daisy", "CV456")

hostel.record_visit(visitor1, resident1)
hostel.record_visit(visitor2, resident2)

hostel.show_visits()

        
        
    



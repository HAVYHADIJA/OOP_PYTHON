class Resident:
    def __init__(self,name,room): #parameters being passed in the brackets are just variables
        self.name = name
        self.roomNumber = room

class Visitor:
    def __init__(self, name , IDno, contact):
        self.name = name
        self.IDno = IDno
        self.phoneNumber = contact

class Hostel:
    def __init__(self, name, location):
        self.hostelName = name
        self.loc = location

        self.visits = []  # List/array to keep track of visits
    def recordVisits(self, visitor:Visitor, resident:Resident):
        entry = visitor.name  +  "is visiting"  +  resident.name  +  "in room"  +  resident.roomNumber
        self.visits.append(entry)

    def showVisits(self):
        print(f"Visits Log for {self.hostelName}:")
        if not self.visits:
            print("No visits recorded yet.")
        else:
            for visit in self.visits:
                print( "-"  +  visit)


# instance of Hostel
hostel = Hostel("David's Ark Hostel", "Ankrah hill")

resident = Resident("Gabriella", "C3")

visitor1 = Visitor( "Havy",  "B2123",  "0709517000")
visitor2 = Visitor( "Daisy",  "CV456",  "0776290776")
visitor3 = Visitor( "Emmanuella",  "D7890", "0774574661")
visitor4 = Visitor( "Kamoga",  "E1234", "0703456789")

hostel.recordVisits( visitor1, resident)
hostel.recordVisits( visitor2, resident)
hostel.recordVisits( visitor3, resident)
hostel.recordVisits( visitor4, resident)

hostel.showVisits()
                
        

  


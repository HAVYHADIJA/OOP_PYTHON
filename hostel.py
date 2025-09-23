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

  


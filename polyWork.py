class Employee:
    def __init__(self,name):
        self.name = name
        
    def calculate_salary(self):
        pass

class Fulltime(Employee):
    def __init__(self,name,Job_Tittle,salary):
        super().__init__()
        self.name = name
        self.Job_Tittle = Job_Tittle
        self.salary =salary
    def calculate_salary(self):
        return self.salary  #Fixed Salary

class Parttime(Employee):
    def __init__(self, name, rate_per_session, sessions):
        super().__init__(name)
        self.rate_per_session = rate_per_session
        self.sessions = sessions

    def calculate_salary(self):
        return self.rate_per_session * self.sessions #Payment based on Sessions

class Intern(Employee):
    def __init__(self, name, supervisor,department, duration_months, lunch_allowance = 0):
        super().__init__(name)
        self.supervisor= supervisor
        self.department = department
        self.duration_months = duration_months
        self.lunch_allowance = lunch_allowance

    def calculate_salary(self):
        # Total pay for the internship period
        return self.lunch_allowance* self.duration_months
    
    def get_intern_details(self):
        return f"Intern: {self.name}, Supervisor: {self.supervisor}, Department: {self.department}, Duration: {self.duration_months} months"

f = Fulltime("Richard", "Developer", 1500000)
p = Parttime("Sarah", 20000, 10)
i = Intern("Havy", "Ms. Grace", "IT Department", 3, 3000)

print


# Polymorphism exampale 2

class PoliticalParty:
    def slogan(self):
        pass


class PartyA(PoliticalParty):
    def slogan(self):
        return "Party A: Our Power"


class PartyB(PoliticalParty):
    def slogan(self):
        return "Party B: Protecting the gains!"


class PartyC(PoliticalParty):
    def slogan(self):
        return "Party C: Empower Servantl_Leadweship!"


# Demonstrating polymorphism
parties = [PartyA(), PartyB(), PartyC()]

for party in parties:
   print(party.slogan())



        
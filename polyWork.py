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
        return self.salary  

class Parttime(Employee):
    def __init__(self, name, rate_per_session, sessions):
        super().__init__(name)
        self.rate_per_session = rate_per_session
        self.sessions = sessions

    def calculate_salary(self):
        return self.rate_per_session * self.sessions 

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


        
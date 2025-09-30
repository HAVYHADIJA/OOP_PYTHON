class Student:
    def __init__(self, name):
        self.name = name #public
        self._gpa = 3.5 #protected
        self.__password = "1234" #private
        
        
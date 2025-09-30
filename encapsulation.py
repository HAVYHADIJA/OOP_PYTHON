class Student:
    def __init__(self, name):
        self.name = name #public
        self._gpa = 3.5 #protected
        self.__password = "1234" #private

#creating an object of the class
student1 = Student("Nakalyowa Hadijah")

print(student1.name)
print(student1._gpa)
print(student1)




        
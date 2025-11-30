class BankAccount:
    def __init__(self,balance = 0.0):
        self.balance = float(balance)
    def deposit(self,amount: float):
        if amount < 0:
            print("Deposit must be postive")
            return
        self.balance += amount
        print(f"Deposited: {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw (self,amount:float):
        if amount < 0:
            print("Withdraw must be positve")
            return
        if amount >self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew: {amount:.2f}. New balance: {self.balance:.2f}")

  
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Final balance: {account.balance:.2f}")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello, My name is {self.name}, and I am {self.age} years old")
student = Student("Zoe", 23)
print(student.introduce())
        
class Phone:
    def __init__(self, brand, storage):
        self.brand = brand
        self.storage = storage
    def make_call(self,phone_number):
        print(f"I am calling {phone_number} from my {self.brand} phone")
    def take_photo(self):
        print(f"Taking a photo with my {self.brand}, {self.storage} is left")

phone = Phone("Iphone13", "256gb")
phone.make_call("0709517000")
phone.take_photo()



#ABSTRACTION
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("You stop the car")

class MotorCycle(Vehicle):
    def go(self):
        print("You ride the MotorCycle")
    def stop(self):
        print("You stop the MotorCycle")

car = Car()
car.go()
car.stop()

motorcycle = MotorCycle()
motorcycle.go()
motorcycle.stop()
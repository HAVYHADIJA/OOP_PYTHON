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
        

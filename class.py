## CLASS IN PYTHON WITHOUT ENCAPSULATION
class ATM:
    def __init__(self,name,pin,account_balance):
        self.name = name
        self.pin = pin
        self.account_balance = account_balance
        
name = "Havy"
pin = 124
account_balance = 1000
atm = ATM(name, pin, account_balance)
print ("This ATM belongs to", atm.name) 
print ("Your account balance is", atm.account_balance)

#here in the above code we can easily change the sensitive values of the class like pin and account_balance


## CLASS IN PYTHON WITH ENCAPSULATION
class ATM:
    def __init__(self, name, pin, account_balance):
        self.name = name
        self.__pin = pin  # private attribute
        self.__account_balance = account_balance  # private attribute

#setter method for pin
    def set_pin(self):
        if pin >= 8:
            self.__pin = pin
            print("Pin set successfully")
        else:
            print("Oops! This pin is invalid")
            
#getter method to access the pin available
    def get_pin(self):
        return self.__pin
#setter method for account balannce
    def set_account_balance(self, amount):
        if amount >= 0:
            self.__account_balance = amount
        else:
            print("Invalid amount. Account balance cannot be negative.")

#getter method to access the account balance
    def get_account_balance(self):
        return self.__account_balance
    





class Car:
    def __init__(self,speed,color):
        print(speed)
        print(color)
        self.speed = speed
        self.color = color
        print ("The __init__ is called")
ford =  Car (200, "Grey")
honda = Car (250 , "Blue")
audi = Car (300 , "Black")
print (ford.speed)
print (audi.color)




        
        
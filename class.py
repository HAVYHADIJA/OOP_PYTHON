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



        
        
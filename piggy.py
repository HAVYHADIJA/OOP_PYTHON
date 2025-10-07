coins = 100
Jacob  = 500
coins = 100 + 500
print("I have ",coins,"coins in my piggy")

class Piggybank:
    def __init__(self,coins):
        self.coins = coins
        self.put_in(coins)
    def put_in(self,amount):
        if amount <= 0:
            raise ValueError("Add real money")
        self.coins += amount

    def take_out(self,amount):
        if amount <= 0:
            raise ValueError("Be real")
        if amount > self.coins:
            raise ValueError("Money is coming")
        self.coins -= amount
        
        

Havy = Piggybank(10000)
print("Havy's Box has",Havy.coins)

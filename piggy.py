coins = 100
Jacob  = 500
coins = 100 + 500
print("I have ",coins,"coins in my piggy")

class Piggybank:
    def __init__(self,coins):
        self.coins = coins
        
Havy = Piggybank(10000)
print("Havy's Box has",Havy.coins)

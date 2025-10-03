class Player:
    def __init__(self, name, attack_power, health=100):
        self.name = name
        self.attack_power = attack_power
        self.health = health
    
    def attack(self,other):
        other.health -= self.attack_power

    def heal(self, amount):
        self.health += amount
        
    def is_alive(self):
        return self.health > 0
    
    player1 = Player("Hero", attack_power = 20)
    player2 = Player("Monster",attack_power = 15)

#ROUND simulation
round_number = 1
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
    
    # Create player instances
player1 = Player("Hero", attack_power = 20)
player2 = Player("Monster", attack_power = 15)

#ROUND simulation
round_number = 1
class Player:
    def _init_(self, name, attack_power, health=100):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, other):
        other.health -= self.attack_power
    
    def heal(self, amount):
        self.health += amount
    
    def is_alive(self):
        return self.health > 0

# Create 2 players with different attack powers
player1 = Player("Havie", attack_power=15)
player2 = Player("Paul", attack_power=12)

# Simulate fight round by round
round_number = 1

print("=== BATTLE BEGINS ===")

while player1.is_alive() and player2.is_alive():
    print(f"\n--- Round {round_number} ---")
    
    # Player 1 attacks Player 2
    player1.attack(player2)
    print(f"{player1.name} attacks {player2.name} for {player1.attack_power} damage!")
    print(f"{player2.name} health: {player2.health}")
    
    # Check if player2 is still alive
    if not player2.is_alive():
        break
    
    # Player 2 attacks Player 1
    player2.attack(player1)
    print(f"{player2.name} attacks {player1.name} for {player2.attack_power} damage!")
    print(f"{player1.name} health: {player1.health}")
    
    round_number += 1

# Determine winner
print(f"\n=== BATTLE ENDS ===")
if player1.is_alive():
    print(f"{player1.name} WINS!")
else:
    print(f"{player2.name} WINS!")
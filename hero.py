from characters import Character 
import random  


class Hero(Character):
    def __init__(self, health=10, power=5, bounty=5, armor=0, evade=0):
        super().__init__("Hero", health, power, bounty)
        self.armor = armor 
        self.evade = evade 

    def attack(self, opponent):
        power_int = random.randint(1, 5)
        agility_int = random.randint(1, opponent.agility)
        if power_int == 5 and agility_int == 1:
            power = self.power * 2
            print("\nSuper attack!")
        elif agility_int == 1:
            power = self.power
        else: 
            print("\nAttack evaded!")
            power = 0
        opponent.health -= power 
        print(f"You do {power} damage to the {opponent.name}.\n")

    def print_status(self):
        print(f"You have {self.health} health.")

    def collect_bounty(self, opponent):
        self.bounty += opponent.bounty
        print(f"Bounty collected! Current amount of coins: {self.bounty}")

    def print_item_status(self):
        print(f"Armor: {self.armor}")
        print(f"Agility: {self.evade + 1}\n")
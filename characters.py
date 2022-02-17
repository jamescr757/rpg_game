import random 


class Character():
    def __init__(self, name, health, power, bounty=5, agility=1):
        self.name = name 
        self.health = health 
        self.power = power 
        self.bounty = bounty
        self.agility = agility

    def attack(self, opponent):
        random_int = random.randint(1, opponent.agility + opponent.evade)
        if random_int == 1 and opponent.armor:
            opponent.health -= self.power + 2
        elif random_int == 1 and not opponent.armor:
            opponent.health -= self.power 
        else:
            print("Attack evaded!")

    def alive(self):
        if self.health < 1:
            return False 
        return True 

    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self, health=10, power=5, bounty=0, armor=0, evade=0):
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
        print(f"You have {self.health} health and {self.power} power.")

    def collect_bounty(self, opponent):
        self.bounty += opponent.bounty
        print(f"Bounty collected! Current amount of coins: {self.bounty}")

class Goblin(Character):
    def __init__(self, health=6, power=2, bounty=5):
        super().__init__("Goblin", health, power, bounty)

class Medic(Character):
    def __init__(self, health=10, power=1, bounty=3, can_recover=True):
        super().__init__("Medic", health, power, bounty)
        self.can_recover = can_recover 

    def recovery(self):
        random_int = random.randint(1, 5)
        if random_int == 5:
            self.health += 2
            print(f"The Medic recovered 2 health points!")

class Shadow(Character):
    def __init__(self, health=1, power=4, bounty=7, agility=10):
        super().__init__("Shadow", health, power, bounty, agility) 

class Zombie(Character):
    def __init__(self, health=1, power=2, bounty=10):
        super().__init__("Zombie", health, power, bounty)

    def alive(self):
        return True
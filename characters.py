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
        if random_int == 1 and opponent.armor and opponent.shield:
            power = self.power - 3 if self.power - 3 >= 0 else 0
        elif random_int == 1 and opponent.armor:
            power = self.power - 2 if self.power - 2 >= 0 else 0
        elif random_int == 1 and opponent.shield:
            power = self.power - 1
        elif random_int == 1:
            power = self.power 
        else:
            power = 0
            print("Attack evaded!")
        opponent.health -= power 
        print(f"The {self.name} does {power} damage to you.\n")

    def alive(self):
        if self.health < 1:
            return False 
        return True 

    def print_status(self):
        print(f"The {self.name} has {self.health} health.")

# The Cobra evades attacks 33% of the time and has lethal venom 20% of the time 
class Cobra(Character):
    def __init__(self, health=8, power=10, bounty=8, agility=3):
        super().__init__("Cobra", health, power, bounty, agility)

    def attack(self, opponent):
        random_int = random.randint(1, 5)
        if random_int == 5:
            power = self.power 
            print("You have been attacked with venom!")
        else:
            power = 0
            print("Attack evaded!")
        opponent.health -= power
        print(f"The {self.name} does {power} damage to you.\n")

# The Goblin evades attacks 50% of the time
class Goblin(Character):
    def __init__(self, health=6, power=4, bounty=5, agility=2):
        super().__init__("Goblin", health, power, bounty, agility)

# The Medic can recover 3 health points 20% of the time 
class Medic(Character):
    def __init__(self, health=10, power=3, bounty=5, can_recover=True):
        super().__init__("Medic", health, power, bounty)
        self.can_recover = can_recover 

    def recovery(self):
        random_int = random.randint(1, 5)
        if random_int == 5:
            self.health += 3
            print(f"The Medic recovered 3 health points!")

# The Scythe can have a super attack 33% of the time 
class Scythe(Character):
    def __init__(self, health=8, power=4, bounty=6):
        super().__init__("Scythe", health, power, bounty)

    def attack(self, opponent):
        power_int = random.randint(1, 3)
        agility_int = random.randint(1, opponent.agility + opponent.evade)
        if power_int == 5 and agility_int == 1:
            if opponent.armor and opponent.shield:
                power = self.power * 2 - 3
            elif opponent.armor:
                power = self.power * 2 - 2
            elif opponent.shield:
                power = self.power * 2 - 1
            else: 
                power = self.power * 2
            print("\nSuper attack!")
        elif agility_int == 1:
            if opponent.armor and opponent.shield:
                power = self.power - 3
            elif opponent.armor:
                power = self.power - 2
            elif opponent.shield:
                power = self.power - 1
            else: 
                power = self.power
        else: 
            print("\nAttack evaded!")
            power = 0
        opponent.health -= power 
        print(f"The {self.name} does {power} damage to you.\n")

# The Shadow evades attacks 90% of the time
class Shadow(Character):
    def __init__(self, health=1, power=4, bounty=7, agility=10):
        super().__init__("Shadow", health, power, bounty, agility) 

# The Wizard can cut through armor and a shield with a magic spell
class Wizard(Character):
    def __init__(self, health=10, power=3, bounty=6):
        super().__init__("Wizard", health, power, bounty)

    def attack(self, opponent):
        random_int = random.randint(1, opponent.agility + opponent.evade)
        if random_int == 1:
            power = self.power 
        else:
            power = 0
            print("Attack evaded!")
        opponent.health -= power 
        print(f"The {self.name} does {power} damage to you.\n")

# The Zombie can live until -50 health points
class Zombie(Character):
    def __init__(self, health=0, power=4, bounty=10):
        super().__init__("Zombie", health, power, bounty)

    def alive(self):
        if self.health <= -50:
            return False
        return True
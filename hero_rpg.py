from characters import *
from hero import Hero 
from items import Item 
import random 


main_menu = """
What do you want to do?
1. Fight
2. Visit Store
3. Flee"""
opponents = [Goblin(), Medic(), Shadow(), Zombie()]
store_items = [Item("Super Tonic", 8), Item("Armor", 4), Item("Evade", 5)]


def select_opponent():
    random_index = random.randint(0, len(opponents) - 1)
    return opponents[random_index]

def display_store_menu():
    print("\nStore Items:")
    for index, item in enumerate(store_items):
        print(f"{index + 1}. {item.name}: {item.cost} coins")
    print()

def get_item_index(user_input):
    try:
        return int(user_input) - 1
    except ValueError:
        print("Thank you for visiting the store.\n")
        return len(store_items) 

def store_visit(hero):
    print(f"You currently have {hero.bounty} coins.")
    hero.print_item_status()
    store_input = input("Enter a number to purchase an item. Anything else to leave the store: ")
    item_index = get_item_index(store_input)
    if item_index < len(store_items):
        item = store_items[item_index]
        store_purchase(item, hero)
        update_hero_with_item(item, hero)

def store_purchase(item, hero):
    if hero.bounty >= item.cost:
        print(f"\nYou have purchased {item.name} for {item.cost} coins.")
        hero.bounty -= item.cost
        print(f"You now have {hero.bounty} coins.\n")
    else:
        print(f"\nYou do not have enough coins to purchase {item.name}.\n")

def update_hero_with_item(item, hero):
    if item.name == "Armor":
        hero.armor = True 
    elif item.name == "Evade":
        hero.evade += 2
    elif item.name == "Super Tonic": 
        hero.health = 10 
    elif item.name == "item4":
        pass 
    elif item.name == "item5": 
        pass          
     
def main():
    hero = Hero()
    opponent = select_opponent()

    while opponent.alive() and hero.alive():
        hero.print_status()
        opponent.print_status()
        print(main_menu)
        raw_input = input("> ")
        if raw_input == "1":
            hero.attack(opponent)
            if not opponent.alive():
                print(f"The {opponent.name} is dead.")
                hero.collect_bounty(opponent)
        elif raw_input == "2":
            display_store_menu()
            store_visit(hero)
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if opponent.alive():
            if hasattr(opponent, "can_recover"):
                opponent.recovery()
            opponent.attack(hero)
            if hero.health <= 0:
                print("You are dead.")


main()


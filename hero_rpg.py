from characters import *
from items import Item 
import random 


main_menu = """
What do you want to do?
1. Fight
2. Visit Store
3. Flee"""
opponents = [Goblin(), Medic(), Shadow(), Zombie()]
store_items = [Item("Super Tonic", 5), Item("Armor", 5), Item("Evade", 5)]


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
        print("Thank you for visiting the store.")
        return len(store_items) 
     

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
            if opponent.health <= 0 and opponent.name != "Zombie":
                print(f"The {opponent.name} is dead.")
                hero.collect_bounty(opponent)
        elif raw_input == "2":
            display_store_menu()
            print(f"You currently have {hero.bounty} coins.")
            store_input = input("Enter a number to purchase an item. Anything else to leave the store.")
            item_index = get_item_index(store_input)
            if item_index < len(store_items):
                item = store_items[item_index]
                if hero.bounty >= item.cost:
                    print(f"You have purchased {item.name} for {item.cost} coins.")
                    hero.bounty -= item.cost
                    print(f"You now have {hero.bounty} coins.")
                else:
                    print(f"You do not have enough coins to purchase {item.name}.")
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if opponent.alive():
            if hasattr(opponent, "can_recover"):
                opponent.recovery()
            opponent.attack(hero)
            print(f"The {opponent.name} does {opponent.power} damage to you.\n")
            if hero.health <= 0:
                print("You are dead.")

main()


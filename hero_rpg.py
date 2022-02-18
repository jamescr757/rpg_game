from characters import *
from hero import Hero 
from items import Item 
import random 


main_menu = """
What do you want to do?
1. Fight
2. Visit Store
3. Flee"""
opponents = [Goblin(), Medic(), Shadow(), Wizard(), Zombie()]
store_items = [Item("Super Tonic", 8), Item("Armor", 4), Item("Evade", 5), Item("Sword", 6), Item("Shield", 2)]
heart_symbol = u'\u2764'


def select_opponent():
    random_index = random.randint(0, len(opponents) - 1)
    return opponents[random_index], random_index

def remove_opponent(index):
    del opponents[index]
    print(f"\nThere are {len(opponents)} enemies left!")

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
    print(f"You currently have {hero.bounty} coin{singular_or_plural(hero.bounty)}.")
    hero.print_item_status()
    store_input = input("Enter a number to purchase an item. Anything else to leave the store: ")
    item_index = get_item_index(store_input)
    if item_index < len(store_items):
        item = store_items[item_index]
        purchase_successful = store_purchase(item, hero)
        if purchase_successful:
            update_hero_with_item(item, hero)

def singular_or_plural(coin_number):
    if coin_number == 1:
        return ""
    return "s"

def store_purchase(item, hero):
    if hero.bounty >= item.cost:
        print(f"\nYou have purchased {item.name} for {item.cost} coins.")
        hero.bounty -= item.cost
        print(f"You now have {hero.bounty} coin{singular_or_plural(hero.bounty)}.\n")
        return True 
    print(f"\nYou do not have enough coins to purchase {item.name}.\n")
    return False

def update_hero_with_item(item, hero):
    if item.name == "Armor":
        hero.armor = True 
    elif item.name == "Evade":
        hero.evade += 2
    elif item.name == "Super Tonic": 
        hero.health = 10 
    elif item.name == "Sword":
        hero.power += 2 
    elif item.name == "Shield": 
        hero.shield = True        
     
def main():
    hero = Hero()
    number_of_lives = 3
    # playing = True
    while opponents and number_of_lives > 0:
        opponent, opponent_index = select_opponent()
        if not hero.alive():
            hero = Hero(8, 4, 0)
            print("You have been stripped of your items and coins. The enemies are still out there...\n")
        print(f"Current opponent: The {opponent.name}\n")
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
                    remove_opponent(opponent_index)
            elif raw_input == "2":
                display_store_menu()
                store_visit(hero)
            elif raw_input == "3":
                # print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))
            if opponent.alive():
                if hasattr(opponent, "can_recover"):
                    opponent.recovery()
                opponent.attack(hero)
                if hero.health <= 0:
                    number_of_lives -= 1
                    print(f"You are dead.\nNumber of lives left: {number_of_lives}\n")
        # continue_playing = input("\nDo you want to keep playing? (Y/N) ").lower()
        # if continue_playing == "n" or continue_playing == "no":
        #     playing = False
    if not opponents:
        print("\nYOU WIN!\nYou killed all the enemies!\n")
    elif number_of_lives == 0:
        print("\nNo more lives left! Please play again.\n")
    else:
        print("\nThanks for playing.\n")


main()


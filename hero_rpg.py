from characters import *
from hero import Hero 
from items import Item 
import random 


main_menu = """
What do you want to do?
1. Fight
2. Visit Store
3. Flee"""
opponents = [Cobra(), Goblin(), Medic(), Scythe(), Shadow(), Wizard(), Zombie()]
store_items = [Item("Armor", 4), Item("Dagger", 2), Item("Evade", 5), Item("Shield", 2), Item("Super Tonic", 6), Item("Sword", 4)]
playing = True


def select_opponent():
    random_index = random.randint(0, len(opponents) - 1)
    return opponents[random_index], random_index

def remove_opponent(index):
    del opponents[index]
    if len(opponents) > 1:
        print(f"\nThere are {len(opponents)} enemies left!")
    elif len(opponents) == 1:
        print(f"\nThere is 1 enemy left!")
    else:
        print(f"\nThere are no enemies left!")

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

def check_current_items(name, hero):
    if name == "Evade" or name == "Super Tonic":
        return False 
    elif name == "Armor":
        return hero.armor 
    elif name == "Shield":
        return hero.shield
    elif name == "Sword":
        if hero.convert_sword(hero.power) == "Yes":
            return True 
    elif name == "Dagger":
        if hero.convert_dagger(hero.power) == "Yes":
            return True
    return False 

def add_an_a(name):
    if name == "Sword" or name == "Dagger" or name == "Shield":
        return "a "
    return ""

def store_purchase(item, hero):
    has_item = check_current_items(item.name, hero)
    if hero.bounty >= item.cost and not has_item:
        print(f"\nYou have purchased {add_an_a(item.name)}{item.name} for {item.cost} coins.")
        hero.bounty -= item.cost
        print(f"You now have {hero.bounty} coin{singular_or_plural(hero.bounty)}.\n")
        return True 
    if has_item:
        print(f"\nYou cannot purchase two {item.name}s.\n") 
    else:
        print(f"\nYou do not have enough coins to purchase {add_an_a(item.name)}{item.name}.\n")
    return False

def update_hero_with_item(item, hero):
    if item.name == "Armor":
        hero.armor = True 
    elif item.name == "Dagger":
        hero.power += 1
    elif item.name == "Evade":
        hero.evade += 2
    elif item.name == "Super Tonic": 
        hero.health = 10 
    elif item.name == "Sword":
        hero.power += 2 
    elif item.name == "Shield": 
        hero.shield = True        
     
def battle(opponent, hero, opponent_index, number_of_lives):
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
            break
        else:
            print("Invalid input {}".format(raw_input))
        if opponent.alive():
            if hasattr(opponent, "can_recover"):
                opponent.recovery()
            opponent.attack(hero)
            if hero.health <= 0:
                print(f"You are dead.\nNumber of lives left: {number_of_lives - 1}\n")
                return number_of_lives - 1
    return number_of_lives

def main():
    hero = Hero()
    number_of_lives = 3
    while opponents and number_of_lives > 0:
        opponent, opponent_index = select_opponent()
        if not hero.alive():
            hero = Hero(8, 4, 0)
            print("You have been stripped of your items and coins. The enemies are still out there...\n")
        print(f"Current opponent: The {opponent.name}\n")
        number_of_lives = battle(opponent, hero, opponent_index, number_of_lives)
    if not opponents:
        print("\nYOU WIN!\n")
    else:
        print("\nNo more lives left! Please play again.\n")


while playing:
    main()
    continue_playing = input("\nDo you want to play again? (Y/N) ").lower()
    if continue_playing == "n" or continue_playing == "no":
        playing = False
    else:
        opponents = [Cobra(), Goblin(), Medic(), Scythe(), Shadow(), Wizard(), Zombie()]
        print("\nThe game has been reset.\n\n\n")


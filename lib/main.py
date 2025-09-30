from player import Player
import pokemon
from time import sleep
import random
from helper_funcs import invalid_input

def player_options(pc):
    print("\n---HOME---\n")
    print("\nPress \'E\' to explore the tall grass.\nPress \'L\' to view your pokemon.\nTo quit press \'Q\'.\n")
    valid_input = False
    while valid_input == False:
        user_input = input().lower()
        match user_input:
            case "q":
                valid_input = True
                return False
            case "e":
                valid_input = True
                return explore(pc)
            case "l":
                valid_input = True
                pc.view_pokemon()
                return True
            case _:
                invalid_input()
                continue            

def encounter_options(pc, wild_pokemon):
    valid_input = False
    while valid_input == False:
        print("Do you want to attempt to catch it? (Y/N)")
        user_input = input().lower()
        match user_input:
            case "y":
                valid_input = True
                pc.use_pokeball(wild_pokemon)
            case "n":
                valid_input = True
                print(f"\n{pc.name} successfully ran away!")
            case _:
                invalid_input()
                continue

def random_encounter():
    encounter = random.choice(pokemon.pokemon_list)
    wild_pokemon = encounter()
    print(f"A wild {wild_pokemon.name} has appeared!\n")
    return wild_pokemon

def explore(pc):
    for i in range(random.randint(1,5)):
        sleep(1)
        print("\n*rustle*\n")
    wild_pokemon = random_encounter()

    encounter_options(pc, wild_pokemon)
    
    return True    

def start_game():
    playing = True

    name = input("Hello, what is your name?\n")

    sleep(1)

    print(f"\nNice to meet you {name}. Here's some pokeballs. Go out there and catch a few pokemon.\n")
    pc = Player(name)

    sleep(1)

    print("Pokeballs added\n")
    while playing:
        sleep(1)
        playing = player_options(pc)
    sleep(1)
    print("\nBye!")

start_game()
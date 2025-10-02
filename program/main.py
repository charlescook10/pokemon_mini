from lib.player import Player
from battles import battle
from lib.pokemon_type import Type
from lib.pokemon import Pokemon
from lib.move import Move
from lib.helper_funcs import invalid_input
from time import sleep
import random

# TYPES

BUG = Type("Bug", ("Grass", "Dark", "Psychic"), ("Fire", "Flying", "Rock"))

DARK = Type("Dark", ("Ghost", "Psychic"), ("Bug", "Fairy", "Fighting"))

DRAGON = Type("Dragon", ("Dragon",), ("Dragon", "Fairy", "Ice"))

ELECTRIC = Type("Electric", ("Flying", "Water"), ("Ground",))

FAIRY = Type("Fairy", ("Fighting", "Dark", "Dragon"), ("Poison", "Steel"))

FIGHTING = Type("Fighting", ("Dark", "Ice", "Normal", "Rock", "Steel"), ("Fairy", "Flying", "Psychic"))

FIRE = Type("Fire", ("Bug", "Grass", "Ice", "Steel"), ("Ground", "Rock", "Water"))

FLYING = Type("Flying", ("Bug", "Fighting", "Grass"), ("Electric", "Ice", "Rock"))

GHOST = Type("Ghost", ("Ghost", "Psychic"), ("Dark", "Ghost"))

GRASS = Type("Grass", ("Ground", "Rock", "Water"), ("Bug", "Fire", "Flying", "Ice", "Poison"))

GROUND = Type("Ground", ("Electric", "Fire", "Poison", "Rock", "Steel"), ("Grass", "Ice", "Water"))

ICE = Type("Ice", ("Dragon", "Flying", "Grass", "Ground"), ("Fighting", "Fire", "Rock", "Steel"))

NORMAL = Type("Normal", (), ("Fighting",))

POISON = Type("Poison", ("Fairy", "Grass"), ("Ground", "Psychic"))

PSYCHIC = Type("Psychic", ("Fighting", "Poison"), ("Bug", "Dark", "Ghost"))

ROCK = Type("Rock", ("Bug", "Fire", "Flying", "Ice"), ("Fighting", "Grass", "Ground", "Steel", "Water"))

STEEL = Type("Steel", ("Fairy", "Ice", "Rock"), ("Fighting", "Fire", "Ground"))

WATER = Type("Water", ("Fire", "Ground", "Rock"), ("Electric", "Grass"))

# MOVES

# Normal

SCRATCH = Move("Scratch", NORMAL, 30)
QUICK_ATTACK = Move("Quick Attack", NORMAL, 30)
TACKLE = Move("Tackle", NORMAL, 30)

# Electric
THUNDER_SHOCK = Move("Thunder Shock", ELECTRIC, 40)

# Water
WATER_GUN = Move("Water Gun", WATER, 40)

# Fire
EMBER = Move("Ember", FIRE, 40)

# Grass
VINE_WHIP = Move("Vine Whip", GRASS, 45)

# Pokemon species

class Charmander(Pokemon):
    def __init__(self, name=False):
        super().__init__("Charmander", [FIRE], random.choice([SCRATCH, EMBER]), name, speed=1.1)

    def cry(self):
        pass

class Bulbasaur(Pokemon):
    def __init__(self, name=False):
        super().__init__("Bulbasaur", [GRASS], random.choice([TACKLE, VINE_WHIP]), name, atk_pwr=1.5, speed=0.9)

    def cry(self):
        pass

class Pikachu(Pokemon):
    def __init__(self, name=False):
        super().__init__("Pikachu", [ELECTRIC], random.choice([QUICK_ATTACK, THUNDER_SHOCK]), name, speed=1.2)

    # If cry did something then it would be an example of polymorphism
    def cry(self):
        pass

class Squirtle(Pokemon):
    def __init__(self, name=False):
        super().__init__("Squirtle", [WATER], random.choice([TACKLE, WATER_GUN]), name, hp=45)

    def cry(self):
        pass

POKEMON = [Pikachu, Charmander, Bulbasaur, Squirtle]

STARTER_POKEMON = [Bulbasaur, Charmander, Squirtle]

def starter_selection(pc):
    print("Choose a starter pokemon.\n(1)Bulbasaur (2)Charmander (3)Squirtle\n")
    valid_input = False
    while valid_input == False:
        user_input = input()
        match user_input:
            case "1":
                valid_input = True
                pc.starter_pokemon(STARTER_POKEMON[0]())
            case "2":
                valid_input = True
                pc.starter_pokemon(STARTER_POKEMON[1]())
            case "3":
                valid_input = True
                pc.starter_pokemon(STARTER_POKEMON[2]())
            case _:
                invalid_input()
                continue

def player_options(pc):
    print("\n---HOME---\n")
    if pc.follower != None:
        pc.follower.heal()
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

def encounter(pc, wild_pokemon):
    battle(pc, wild_pokemon)

def random_encounter():
    encounter = random.choice(POKEMON)
    wild_pokemon = encounter()
    print(f"A {wild_pokemon.name} has appeared!\n")
    return wild_pokemon

def explore(pc):
    for i in range(random.randint(1,5)):
        sleep(1)
        print("\n*rustle*\n")
    wild_pokemon = random_encounter()

    encounter(pc, wild_pokemon)
    
    return True    

def start_game():
    playing = True

    name = input("Hello, what is your name?\n")

    sleep(1)

    print(f"\nNice to meet you {name}. Here's some pokeballs. Go out there and catch a few pokemon.\n")
    pc = Player(name)

    sleep(1)

    print("Pokeballs added\n")

    sleep(1)
    
    starter_selection(pc)

    while playing:
        sleep(1)
        playing = player_options(pc)
    sleep(1)
    print("\nBye!")

start_game()
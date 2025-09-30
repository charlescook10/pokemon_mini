import pokemon_types
from helper_funcs import invalid_input

def calculate_effectiveness():
    pass

def calculate_dmg_done():
    pass

def is_fainted():
    pass

def battle_options(pc):
    while valid_input == False:
        print("\nAttack(A), Throw pokeball(P), Run Away(R)\n")
        user_input = input().lower()
        match user_input:
            case "a":
                valid_input = True
            case "p":
                valid_input = True
            case "r":
                valid_input = True
            case _:
                invalid_input()
                continue

def battle(pc, wild_pokemon):
    pokemon_can_battle = True
    while pokemon_can_battle:
        print()
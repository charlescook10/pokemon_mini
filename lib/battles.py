from helper_funcs import invalid_input

from time import sleep
import random

def calculate_effectiveness(move, pokemon_type):
    effectiveness = 1.0
    for type in pokemon_type:
        #print(move.type.type in type.weak_against)
        if move.type.type in type.weak_against:
            effectiveness = effectiveness*2
        
        #print(move.type.type in type.weak_against)
        if move.type.type in type.strong_against:
            effectiveness = effectiveness/2
    #print(f"Effectiveness of {move.name}: {effectiveness}")
    return effectiveness


def calculate_dmg_done(pokemon, target_pokemon):
    effectiveness = calculate_effectiveness(pokemon.move(), target_pokemon.type)
    dmg = int((((pokemon.move().pwr)*pokemon.atk_pwr + 4)/5) * effectiveness)
    sleep(1.5)
    pokemon.attack(target_pokemon, dmg)
    return dmg

def fainted_check(pokemon):
    if pokemon.is_fainted:
        sleep(1)
        print(f"{pokemon.name} has fainted!")
    return pokemon.is_fainted

def fight(first_pokemon, second_pokemon):
    print(f"\n{first_pokemon.name} went first!\n")
    if second_pokemon.take_dmg(calculate_dmg_done(first_pokemon, second_pokemon)) != True:
        if first_pokemon.take_dmg(calculate_dmg_done(second_pokemon, first_pokemon)) == True:
            return True
    else:
        return True

def battle_order(pc_pokemon, wild_pokemon):
    if pc_pokemon.speed >= wild_pokemon.speed:
        return fight(pc_pokemon, wild_pokemon)
    else:
        return fight(wild_pokemon, pc_pokemon)

def battle_options(pc, wild_pokemon):
    while True:
        print("\nAttack(A), Throw pokeball(P), Run Away(R)\n")
        user_input = input().lower()
        match user_input:
            case "a":
                if battle_order(pc.follower_pokemon, wild_pokemon):
                    return
            case "p":
                if pc.throw_pokeball(wild_pokemon):
                    return
                else:
                    continue
            case "r":
                if random.random() > 0.1:
                    print(f"\n{pc.name} successfully ran away!\n")
                    return
                else:
                    print(f"\n{pc.name} failed to run away!\n")
                    continue
            case _:
                invalid_input()
                continue

def battle(pc, wild_pokemon):
    pokemon_can_battle = True
    while pokemon_can_battle:
        pokemon_can_battle = battle_options(pc, wild_pokemon)
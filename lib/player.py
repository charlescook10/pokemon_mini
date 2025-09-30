import random
from time import sleep
from helper_funcs import invalid_input

class Player():
    def __init__(self, name):
        self.name = name
        self.follower_pokemon = None
        self.pokemon = []
    def __give_pokemon_name(self, pokemon):
        valid_input = False
        while valid_input == False:
            user_input = input().lower()
            match user_input:
                case "y":
                    valid_input = True
                    print("Enter a name:")
                    pokemon.name = input()
                case "n":
                    valid_input = True
                    pokemon.name = pokemon.species
                case _:
                    invalid_input()
                    continue 
    def throw_pokeball(self, pokemon):
        counter = 0
        print(f"\n{self.name} threw a pokeball!\n")
        for x in range(3):
            sleep(1)
            if random.random() > 0.15:
                counter+=1
                print("Ding!\n")
            else:
                print(f"{pokemon.name} escaped!\n")
                break
        if counter == 3:
            print(f"Congratulations! You caught a {pokemon.species}.\n")
            pokemon.is_wild = False
            print(f"\nWould you like to give {pokemon.species} a name?(Y/N)")
            self.__give_pokemon_name(pokemon)
            self.pokemon.append(pokemon)
            print(f"\n{pokemon.name} added to your collection.\n")
            if self.follower_pokemon == None:
                self.set_as_follower(pokemon)
            return True
        return False
    def starter_pokemon(self, pokemon):
        print(f"\nWould you like to give {pokemon.species} a name?(Y/N)")
        self.__give_pokemon_name(pokemon)
        self.pokemon.append(pokemon)
        print(f"\n{pokemon.name} added to your collection.\n")
        if self.follower_pokemon == None:
            self.set_as_follower(pokemon)
    def view_pokemon(self):
        print(f"\n---{self.name} Pokemon---\n")
        for pokemon in self.pokemon:
            print(f"\n{pokemon}")
    def set_as_follower(self, pokemon):
        self.follower_pokemon = pokemon
        print(f"\n{self.follower_pokemon.name} is now following you.")
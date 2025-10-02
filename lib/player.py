import random
from time import sleep
from helper_funcs import invalid_input
from pokemon import Pokemon

class Player():
    def __init__(self, name="Stranger"):
        self._name = name
        self._follower_pokemon = None
        self._pokemon = []
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name

    name = property(get_name, set_name)

    def get_follower(self):
        return self._follower_pokemon

    def set_follower(self, pokemon):
        if isinstance(pokemon, Pokemon):
            self._follower_pokemon = pokemon
            print(f"\n{self._follower_pokemon.name} is now following you.")

    follower = property(get_follower, set_follower)

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
                    pokemon.name = pokemon.get_species()
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
            print(f"Congratulations! You caught a {pokemon.get_species()}.\n")
            pokemon.wild = False
            print(f"\nWould you like to give {pokemon.get_species()} a name?(Y/N)")
            self.__give_pokemon_name(pokemon)
            self._pokemon.append(pokemon)
            print(f"\n{pokemon.name} added to your collection.\n")
            if self._follower_pokemon == None:
                self.set_follower(pokemon)
            return True
        return False
    
    def starter_pokemon(self, pokemon):
        print(f"\nWould you like to give {pokemon.get_species()} a name?(Y/N)")
        self.__give_pokemon_name(pokemon)
        self._pokemon.append(pokemon)
        print(f"\n{pokemon.name} added to your collection.\n")
        if self._follower_pokemon == None:
            self.set_follower(pokemon)

    def view_pokemon(self):
        print(f"\n---{self.name} Pokemon---\n")
        for pokemon in self._pokemon:
            print(f"\n{pokemon}")
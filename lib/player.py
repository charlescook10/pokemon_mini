import random
from time import sleep
class Player():
    def __init__(self, name):
        self.name = name
        self.pokemon = []
    def use_pokeball(self, pokemon):
        counter = 0
        for x in range(3):
            sleep(1)
            if random.random() > 0.15:
                counter+=1
                print("Ding!\n")
            else:
                print(f"{pokemon.name} escaped!\n")
        if counter == 3:
            print(f"Congratulations! You caught a {pokemon.name}.\n\n")
            self.pokemon.append(pokemon)
            return True
        return False
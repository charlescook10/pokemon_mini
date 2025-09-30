from abc import ABC, abstractmethod
import pokemon_types
import moves
import random

class Pokemon(ABC):
    def __init__(self, species, types, move, name=False):
        self._species = species
        self.type = types
        self.name = name if name else species
        self._learnt_move = move

        self.hp = 40
        self.atk_pwr = 1
        self.speed = 1

    def __str__(self):
        return_string = ""
        if self.name == self._species:
            return_string = f"{self.name} a {self.type[0]}"
        else:
            return_string = f"{self.name} a {self._species} an {self.type[0]}"
        for type in self.type[1:]:
            return_string += f", {type}"
        return_string += " type pokemon\n\n"
        return return_string
    def take_dmg(self, move):
        pass
    def move(self):
        return self._learnt_move
    @abstractmethod
    def cry(self):
        # makes the pokemon species sound
        pass
    @abstractmethod
    def attack(self, pokemon):
        pass

class Pikachu(Pokemon):
    def __init__(self, name=False):
        super().__init__("Pikachu", [pokemon_types.electric], random.choice([moves.quick_attack, moves.thunder_shock]), name)
    def cry(self):
        pass
    def attack(self, pokemon):
        print(f"{self.name} uses {self._learnt_move} on {pokemon.name}!")
    def give_name(self, name):
        self.name = name

class Charmander(Pokemon):
    def __init__(self, name=False):
        super().__init__("Charmander", [pokemon_types.fire], moves.scratch, name)
    def cry(self):
        pass
    def attack(self, pokemon):
        print(f"{self.name} uses {self._learnt_move} on {pokemon.name}!")
    def give_name(self, name):
        self.name = name


pokemon_list = [Charmander, Pikachu]
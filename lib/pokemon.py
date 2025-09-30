from abc import ABC, abstractmethod
import pokemon_types
import moves
import random

# This would be an example of an abstract class. Can not be instantiated. 

class Pokemon(ABC):
    def __init__(self, species, types, move, name=False, hp=40, atk_pwr=1, defence=1, speed=1):
        self.species = species
        self.type = types
        self._learnt_move = move
        self.is_wild = True
        if name:
            self.name = name
        elif self.is_wild:
            self.name = f"Wild {species}"
        else:
            self.name = species
        self.hp = hp
        self.atk_pwr = atk_pwr
        self.defence = defence
        self.speed = speed
        self.current_hp = hp
        self.is_fainted = False
    def __str__(self):
        return_string = ""
        if self.name == self.species:
            return_string = f"{self.name} a {self.type[0]}"
        else:
            return_string = f"{self.name} a {self.species} an {self.type[0]}"
        for type in self.type[1:]:
            return_string += f", {type}"
        return_string += " type pokemon\n\n"
        return return_string
    def take_dmg(self, dmg):
        self.current_hp = self.current_hp - dmg
        if self.current_hp <= 0:
            self.is_fainted = True
            print(f"{self.name} has fainted!\n")
        else:
            print(f"{self.name} has {self.current_hp} hp remaining.\n")
        return self.is_fainted
    def heal(self):
        self.current_hp = self.hp
        self.is_fainted = False
        print(f"{self.name} has been healed!\n")
    def move(self):
        return self._learnt_move
    def give_name(self, name):
        self.name = name    
    def attack(self, pokemon, dmg):
        print(f"{self.name} uses {self._learnt_move.name} on {pokemon.name}!\n It did {dmg} damage!\n")
    
    @abstractmethod
    def cry(self):
        # makes the pokemon species sound
        pass

# Pokemon is a parent class that the other classes inherit from.

class Pikachu(Pokemon):
    def __init__(self, name=False):
        super().__init__("Pikachu", [pokemon_types.electric], random.choice([moves.quick_attack, moves.thunder_shock]), name)
    # If cry did something then it would be an example of polymorphism
    def cry(self):
        pass

class Charmander(Pokemon):
    def __init__(self, name=False):
        super().__init__("Charmander", [pokemon_types.fire], moves.scratch, name)
    def cry(self):
        pass
    


pokemon_list = [Charmander, Pikachu]
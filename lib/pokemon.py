from abc import ABC, abstractmethod
from move import Move
from pokemon_type import Type
# This would be an example of an abstract class. Can not be instantiated.
# Pokemon is a parent class that the other classes inherit from.

class Pokemon(ABC):
    def __init__(self, species, types, move, name=False, hp=40, atk_pwr=1, defence=1, speed=1):
        self._species = species
        self._type = types
        self._learnt_move = move
        self._is_wild = True
        if name:
            self._name = name
        elif self._is_wild:
            self._name = f"Wild {species}"
        else:
            self.name = species
        self._hp = hp
        self._atk_pwr = atk_pwr
        self._defence = defence
        self._speed = speed
        self._current_hp = hp
        self._is_fainted = False
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name

    def get_move(self):
        return self._learnt_move
    
    def set_move(self, move):
        if isinstance(move, Move):
            self._learnt_move = move

    def get_speed(self):
        return self._speed
    
    def set_speed(self, speed):
        if isinstance(speed, float) or isinstance(speed, int):
            self._speed = speed

    def get_species(self):
        return self._species
    
    def get_wild(self):
        return self._is_wild
    
    def set_wild(self, wild):
        if isinstance(wild, bool):
            self._is_wild = wild
    
    def get_type(self):
        return self._type
    
    def set_type(self, type):
        if isinstance(type, Type):
            self._type = type
    
    name = property(get_name, set_name)
    move = property(get_move, set_move)
    speed = property(get_speed, set_speed)
    wild = property(get_wild, set_wild)
    type = property(get_type, set_type)
    
    def __str__(self):
        return_string = ""
        if self.name == self._species:
            return_string = f"{self.name} a {self._type[0]}"
        else:
            return_string = f"{self.name} a {self._species} a {self._type[0]}"
        for type in self._type[1:]:
            return_string += f", {type}"
        return_string += " type pokemon\n\n"
        return return_string
    
    def take_dmg(self, dmg):
        self._current_hp = self._current_hp - dmg
        if self._current_hp <= 0:
            self._is_fainted = True
            print(f"{self.name} has fainted!\n")
        else:
            print(f"{self.name} has {self._current_hp} hp remaining.\n")
        return self._is_fainted
    
    def heal(self):
        self.current_hp = self._hp
        self.is_fainted = False
        print(f"{self.name} has been healed!\n")

    def get_move_name(self):
        return self._learnt_move.name

    def attack(self, pokemon, dmg):
        print(f"{self.name} uses {self.get_move_name()} on {pokemon.name}!\n It did {dmg} damage!\n")

    def move_pwr(self):
        return self._atk_pwr*self._learnt_move.pwr
    
    def is_fainted(self):
        return self._is_fainted
    
    @abstractmethod
    def cry(self):
        # makes the pokemon species sound
        pass
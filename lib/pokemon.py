from abc import ABC, abstractmethod
import pokemon_types

class Pokemon(ABC):
    def __init__(self, species, types, name=False):
        self._species = species
        self._type = types
        self._name = name if name else species
    def __str__(self):
        return_string = ""
        if self._name == self._species:
            return_string = f"{self._name} an {self._type[0]}"
        else:
            return_string = f"{self._name} a {self._species} an {self._type[0]}"
        for type in self._type[1:]:
            return_string += f", {type}"
        return_string += " type pokemon\n\n"
        return return_string

    @abstractmethod
    def cry(self):
        # makes the pokemon species sound
        pass
    @abstractmethod
    def attack(self):
        pass
    def set_name(self, name):
        self._name = name

class Pikachu(Pokemon):
    def __init__(self, name=False):
        super().__init__("Pikachu", [pokemon_types.electric], name)
    def cry(self):
        pass
    def attack(self):
        print(f"{self._name} uses Thunderbolt!")
    def give_name(self, name):
        self.set_name(name)

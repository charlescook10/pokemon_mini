# pokemon_types = ("Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", 
# "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy")

class Type():
    def __init__(self, type, strong, weak):
        self.type = type
        self.strong_against = strong
        self.weak_against = weak
    def __str__(self):
        return f"{self.type}"
    def effectiveness(self):
        return_string = f"{self.__type} Type\n\nStrong against:"
        for type in self.strong_against:
            return_string += "\n "+type
        return_string += "\n\nWeak against:"
        for type in self.weak_against:
            return_string += "\n "+type
        return return_string

bug = Type("Bug", ("Grass", "Dark", "Psychic"), ("Fire", "Flying", "Rock"))

dark = Type("Dark", ("Ghost", "Psychic"), ("Bug", "Fairy", "Fighting"))

dragon = Type("Dragon", ("Dragon",), ("Dragon", "Fairy", "Ice"))

electric = Type("Electric", ("Flying", "Water"), ("Ground",))

fairy = Type("Fairy", ("Fighting", "Dark", "Dragon"), ("Poison", "Steel"))

fighting = Type("Fighting", ("Dark", "Ice", "Normal", "Rock", "Steel"), ("Fairy", "Flying", "Psychic"))

fire = Type("Fire", ("Bug", "Grass", "Ice", "Steel"), ("Ground", "Rock", "Water"))

flying = Type("Flying", ("Bug", "Fighting", "Grass"), ("Electric", "Ice", "Rock"))

ghost = Type("Ghost", ("Ghost", "Psychic"), ("Dark", "Ghost"))

grass = Type("Grass", ("Ground", "Rock", "Water"), ("Bug", "Fire", "Flying", "Ice", "Poison"))

ground = Type("Ground", ("Electric", "Fire", "Poison", "Rock", "Steel"), ("Grass", "Ice", "Water"))

ice = Type("Ice", ("Dragon", "Flying", "Grass", "Ground"), ("Fighting", "Fire", "Rock", "Steel"))

normal = Type("Normal", (), ("Fighting",))

poison = Type("Poison", ("Fairy", "Grass"), ("Ground", "Psychic"))

psychic = Type("Psychic", ("Fighting", "Poison"), ("Bug", "Dark", "Ghost"))

rock = Type("Rock", ("Bug", "Fire", "Flying", "Ice"), ("Fighting", "Grass", "Ground", "Steel", "Water"))

steel = Type("Steel", ("Fairy", "Ice", "Rock"), ("Fighting", "Fire", "Ground"))

water = Type("Water", ("Fire", "Ground", "Rock"), ("Electric", "Grass"))
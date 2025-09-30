# all moves will have a type and power=dmg done
class Move():
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power
    def use_move(self, pokemon):
        pokemon.take_dmg(self)
    def __str__(self):
        return f"{self.name} a {self.type} type move with {self.power} power."

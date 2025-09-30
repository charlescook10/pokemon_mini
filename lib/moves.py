import pokemon_types

# all moves will have a type and power=dmg done
class Move():
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.pwr = power
    def __str__(self):
        return f"{self.name} a {self.type} type move with {self.pwr} power."

scratch = Move("Scratch", pokemon_types.normal, 40)
quick_attack = Move("Quick Attack", pokemon_types.normal, 40)
thunder_shock = Move("Thunder Shock", pokemon_types.electric, 40)
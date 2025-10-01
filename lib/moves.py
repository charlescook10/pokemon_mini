import pokemon_types

# all moves will have a type and power=dmg done
class Move():
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.pwr = power
    def __str__(self):
        return f"{self.name} a {self.type} type move with {self.pwr} power."
    def effectiveness(self, type, effectiveness):
        if self.type.type in type.weak_against:
            effectiveness = effectiveness*2
        
        if self.type.type in type.strong_against:
            effectiveness = effectiveness/2
        return effectiveness
# Normal
scratch = Move("Scratch", pokemon_types.normal, 30)
quick_attack = Move("Quick Attack", pokemon_types.normal, 30)
tackle = Move("Tackle", pokemon_types.normal, 30)

# Electric
thunder_shock = Move("Thunder Shock", pokemon_types.electric, 40)

# Water
water_gun = Move("Water Gun", pokemon_types.water, 40)

# Fire
ember = Move("Ember", pokemon_types.fire, 40)

# Grass
vine_whip = Move("Vine Whip", pokemon_types.grass, 45)


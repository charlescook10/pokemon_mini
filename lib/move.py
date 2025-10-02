from pokemon_type import Type

# all moves will have a type and power=dmg done
class Move():
    def __init__(self, name, type, power):
        self._name = name
        self._type = type
        self._pwr = power

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
    
    name = property(get_name, set_name)

    def get_type(self):
        return self._type.type

    def set_type(self, type):
        if isinstance(type, Type):
            self._type = type
    
    type = property(get_type, set_type)


    def get_pwr(self):
        return self._pwr

    def set_pwr(self, pwr):
        if isinstance(pwr, int):
            self._pwr = pwr
    
    pwr = property(get_pwr, set_pwr)

    def __str__(self):
        return f"{self._name} a {self._type} type move with {self._pwr} power."
    
    def effectiveness(self, type, effectiveness):
        if self.get_type() in type.weak_against:
            effectiveness = effectiveness*2
        
        if self.get_type() in type.strong_against:
            effectiveness = effectiveness/2
        return effectiveness
    
# Example
# scratch = Move("Scratch", pokemon_types.normal, 30)

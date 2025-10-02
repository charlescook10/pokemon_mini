# pokemon_types = ("Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", 
# "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy")

class Type():
    def __init__(self, type, strong, weak):
        self._type = type
        self._strong_against = strong
        self._weak_against = weak

    def __str__(self):
        return f"{self._type}"
    
    def effectiveness(self):
        return_string = f"{self._type} Type\n\nStrong against:"
        for type in self._strong_against:
            return_string += "\n "+type
        return_string += "\n\nWeak against:"
        for type in self._weak_against:
            return_string += "\n "+type
        return return_string
    
    def get_type(self):
        return self._type
    
    def set_type(self, type_name):
        if isinstance(type_name, str):
            self._type = type_name
    
    def get_strengths(self):
        return self._strong_against
    
    def set_strengths(self, strengths):
        if isinstance(strengths, tuple[str, ...]):
            self._strong_against = strengths

    def get_weaknesses(self):
        return self._weak_against
    
    def set_weaknesses(self, weaknesses):
        if isinstance(weaknesses, tuple[str, ...]):
            self._strong_against = weaknesses

    type = property(get_type, set_type)
    strong_against = property(get_strengths, set_strengths)
    weak_against = property(get_weaknesses, set_weaknesses)


# Example 
# bug = Type("Bug", ("Grass", "Dark", "Psychic"), ("Fire", "Flying", "Rock"))
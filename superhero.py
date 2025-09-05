# superhero.py

class Superhero:
    def __init__(self, name, alias, power, universe):
        self.name = name
        self.alias = alias
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.alias}, also known as {self.name} from the {self.universe} universe!"

    def use_power(self):
        return f"{self.alias} uses {self.power}!"


# Subclass with inheritance and encapsulation
class Mutant(Superhero):
    def __init__(self, name, alias, power, universe, mutation_type):
        super().__init__(name, alias, power, universe)
        self.__mutation_type = mutation_type  # Encapsulated attribute

    def get_mutation(self):
        return f"{self.alias} is a mutant with {self.__mutation_type} mutation."

    def use_power(self):
        return f"{self.alias} unleashes their mutant ability: {self.power}!"


# Sample usage
if __name__ == "__main__":
    hero1 = Superhero("Clark Kent", "Superman", "Flight and Super Strength", "DC")
    print(hero1.introduce())
    print(hero1.use_power())

    mutant1 = Mutant("Jean Grey", "Phoenix", "Telekinesis", "Marvel", "Omega-Level Psychic")
    print(mutant1.introduce())
    print(mutant1.use_power())
    print(mutant1.get_mutation())

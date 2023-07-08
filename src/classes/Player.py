from .Entity import Entity


class Player(Entity):
    def __init__(self, name, health, strength, intelligence, gold):
        super().__init__(name, health, strength)

        self.gold = gold
        self.intelligence = intelligence

    def show_stats(self):
        print("STATS -------------")
        print(f"> Health: {self.health}")
        print(f"> Strength: {self.strength}")
        print(f"> Intelligence: {self.intelligence}")
        print(f"> Gold: {self.gold}")
        print("------------- STATS")

    def magic_attack(self, target):
        magic_damage = self.intelligence / 2
        print(f"{self.name} ATTACKS {target.name}! ({magic_damage} magic damage)")
        target.health -= magic_damage if target.weak_to_magic else 0

    def get_stat(self, stat):
        return getattr(self, stat, None)

    def set_stat(self, stat, value):
        return setattr(self, stat, value)

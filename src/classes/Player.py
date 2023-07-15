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
        magic_damage = self.intelligence / 2 if target.weak_to_magic else 0
        print(f"{self.name} ATTACKS {target.name}! ({magic_damage} magic damage)")
        target.health -= magic_damage

    def get_stat(self, stat):
        return getattr(self, stat, None)

    def set_stat(self, stat, value):
        return setattr(self, stat, value)

    def upgrade_stat(self, stat):
        price_of_new_stat = self.get_stat(stat) * 1.5
        print(f"Price to upgrade {stat} is {price_of_new_stat} gold.")

        if self.gold < price_of_new_stat:
            print("You do not have enough gold.")
            return

        answer = None
        while answer not in ("y", "n"):
            answer = input(f"Would you like to upgrade your {stat}? < [y]es, [n]o > ")

        if answer == "y":
            self.gold -= price_of_new_stat
            self.set_stat(stat, self.get_stat(stat) + 2)
            print(f"You have upgraded your {stat} to {self.get_stat(stat)}!")

    def add_gold(self, gold_to_add):
        new_total_gold = self.gold + gold_to_add

        print(f"GOLD: {self.gold} + {gold_to_add} = {new_total_gold}")

        self.gold = new_total_gold

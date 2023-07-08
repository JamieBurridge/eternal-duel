from .Entity import Entity


class Monster(Entity):
    def __init__(self, name, health, strength, weak_to_magic, gold_for_defeating):
        super().__init__(name, health, strength)

        self.weak_to_magic = weak_to_magic
        self.gold_for_defeating = gold_for_defeating

from .Entity import Entity


class Monster(Entity):
    def __init__(self, name, health, strength, weak_to_magic, gold_for_defeating):
        super().__init__(name, health, strength)

        self.weak_to_magic = weak_to_magic
        self.gold_for_defeating = gold_for_defeating


monster_pixie = Monster("Pixie", 10, 15, False, 20)
monster_goblin = Monster("Goblin", 10, 16, True, 25)
monster_orc = Monster("Orc", 20, 20, True, 40)

monsters = (monster_pixie, monster_goblin, monster_orc)
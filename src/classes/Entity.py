class Entity:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, target):
        damage = self.strength / 2
        print(f"{self.name} ATTACKS {target.name}! ({damage} damage)")
        target.health -= damage

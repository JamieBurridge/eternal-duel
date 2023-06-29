def main():
    player = Player("Jay", 10, 10,10,  20)

    game_is_over = False
    while game_is_over == False:
        monster = Monster("Pixie", 10, 15, True, 20)

        option = None
        while option not in ("f", "s", "e"): option = input("What do you want to do? < [f]ight, [s]tats, [e]xit > ")
        
        if option.lower() == "f":
            fight_loser = fight(player, monster)

            if fight_loser == monster:
                # Player wins
                print("Player won! Here is your reward!")
                player.gold = gold_reward(player, monster)
            else: 
                # Take away gold and restore health
                player.health = player.max_health
        elif option.lower() == "s":
            player.show_stats()
        elif option.lower() == "e":
            game_is_over = True
            break;



#### Entity shared class
class Entity:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength


    def attack(self, target):
        damage = self.strength / 2
        print(f"{self.name} attacks {target.name}! ({damage} damage)")
        target.health -= damage


#### Player setup
class Player(Entity):
    def __init__(self, name, health, strength, intelligence, gold):
        super().__init__(name, health, strength)

        self.max_health = health
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
        print(f"{self.name} attacks {target.name}! ({magic_damage} magic damage)")
        target.health -= magic_damage if target.weak_to_magic else 0


#### Monster setup
class Monster(Entity):
     def __init__(self, name, health, strength, weak_to_magic, gold_for_defeating):
        super().__init__(name, health, strength)
        self.weak_to_magic = weak_to_magic
        self.gold_for_defeating = gold_for_defeating


#### Combat
def fight(player, monster):
    participants = (player, monster)    
    turn_index = 0

    battle_is_over = False

    while battle_is_over == False:
        current_attacker = participants[turn_index]
        print(f">>> {current_attacker.name}'s turn...")

        if current_attacker.health <= 0:
            battle_is_over = True
            break

        if current_attacker == player:
            option = None
            while option not in ("f", "m"): option = input("What do you want to do? [f, m, ?] ")

            if option.lower() == "f":
                player.attack(monster)
            elif option.lower() == "m":
                player.magic_attack(monster)
        else:
            monster.attack(participants[0 if turn_index == 1 else 1])

        turn_index = 0 if turn_index == 1 else 1

        print(f"Monster health: {monster.health} // Player health: {player.health}")
    
    print(f"The loser is {participants[turn_index].name}")
    return participants[turn_index]


#### Post combat
def gold_reward(player, defeated_monster):
    new_total_gold = player.gold + defeated_monster.gold_for_defeating

    print(f"GOLD: {player.gold} + {defeated_monster.gold_for_defeating} = {new_total_gold}")

    print(new_total_gold)
    return new_total_gold


main()



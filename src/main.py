from time import sleep

PRINT_SLEEP_TIME = 2

menu_options = ("f", "s", "u", "e")

stats = {
    "h": "health",
    "s": "strength",
    "i": "intelligence"
}

def main():
    player = Player("Jay", 10, 10, 10, 20)

    game_is_over = False
    while game_is_over == False:
        monster = Monster("Pixie", 10, 15, True, 20)

        option = None
        while option not in menu_options:
            option = input("What do you want to do? < [f]ight, [s]tats, [u]pgrade, [e]xit > ")

        if option.lower() == "f":
            fight_loser = fight(player, monster)

            if fight_loser == monster:
                # Player wins
                print(f"{player.name} WON! Here is your reward!")
                player.gold = gold_reward(player, monster)

        elif option.lower() == "s":
            player.show_stats()
        elif option.lower() == "u":
            stat_to_upgrade = None
            while stat_to_upgrade not in ("h", "s", "i"):
                stat_to_upgrade = input("What stat would you like to upgrade? < [h]ealth, [s]trength, [i]ntelligence > ")

            upgrade_stat(player, stats[stat_to_upgrade])
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
        print(f"{self.name} ATTACKS {target.name}! ({damage} damage)")
        target.health -= damage


#### Player setup
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


#### Monster setup
class Monster(Entity):
     def __init__(self, name, health, strength, weak_to_magic, gold_for_defeating):
        super().__init__(name, health, strength)

        self.weak_to_magic = weak_to_magic
        self.gold_for_defeating = gold_for_defeating


#### Combat
def fight(player, monster):
    player_max_health = player.health
    participants = (player, monster)    
    turn_index = 0

    print(f"A {monster.name} has appeared!!")

    battle_is_over = False
    while battle_is_over == False:
        current_attacker = participants[turn_index]
        sleep(PRINT_SLEEP_TIME)
        print(f">>> {current_attacker.name}'s turn...")

        if current_attacker.health <= 0:
            battle_is_over = True
            break

        if current_attacker == player:
            option = None
            while option not in ("f", "m"): option = input("What do you want to do? < [f]ight, [m]agic > ")

            if option.lower() == "f":
                player.attack(monster)
            elif option.lower() == "m":
                player.magic_attack(monster)
        else:
            sleep(PRINT_SLEEP_TIME)
            monster.attack(participants[0 if turn_index == 1 else 1])

        turn_index = 0 if turn_index == 1 else 1

        print(f"{monster.name}'s health: {monster.health}")
        print(f"{player.name}'s health: {player.health}")
    
    print(f"The loser is {participants[turn_index].name}")

    # Restore player health
    player.health = player_max_health

    # Return the loser
    return participants[turn_index]


#### Post combat
def gold_reward(player, defeated_monster):
    new_total_gold = player.gold + defeated_monster.gold_for_defeating

    print(f"GOLD: {player.gold} + {defeated_monster.gold_for_defeating} = {new_total_gold}")

    return new_total_gold


#### Upgrade
def upgrade_stat(player, stat):
    price_of_new_stat = player.get_stat(stat) * 1.5
    print(f"Price to upgrade {stat} is {price_of_new_stat}")

    if player.gold < price_of_new_stat:
        print("You do no have enough gold")
        return
    
    answer = None
    while answer not in ("y", "n"):
        answer = input(f"Would you like to upgrade your {stat}? < [y]es, [n]o > ")

    if answer == "y":
        player.gold -= price_of_new_stat
        player.set_stat(stat, player.get_stat(stat) + 2)
        print(f"You have upgrade your {stat} to {player.get_stat(stat)}")



main()



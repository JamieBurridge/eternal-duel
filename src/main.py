from classes.Player import Player
from classes.Monster import Monster, monsters

from gameplay.fight import fight

from utils.options import main_menu_options, upgrade_options
from utils.game_states import load_game, save_game

from random import randint


def main():
    # Load game if exists or create new save
    game_load_json = load_game()
    player = Player(game_load_json["name"], game_load_json["health"], game_load_json["strength"], game_load_json["intelligence"], game_load_json["gold"]) if game_load_json else Player("Player", 30, 10, 10, 20)

    while True:
        monster = monsters[randint(0, len(monsters) - 1)]

        option = None
        while option not in main_menu_options.keys():
            option = input("What do you want to do? < [f]ight, [s]tats, [u]pgrade, [e]xit > ")

        # Fight
        if option.lower() == "f":
            fight_loser = fight(player, monster)

            if fight_loser == monster:
                # Player wins
                print(f"{player.name} WON! Here is your reward!")
                player.add_gold(monster.gold_for_defeating)
            else:
                print("You wake up after a long rest...")

        # Show stats
        elif option.lower() == "s":
            player.show_stats()

        # Upgrade
        elif option.lower() == "u":
            stat_to_upgrade = None
            while stat_to_upgrade not in upgrade_options.keys():
                stat_to_upgrade = input("What stat would you like to upgrade? < [h]ealth, [s]trength, [i]ntelligence > ")

            player.upgrade_stat(upgrade_options[stat_to_upgrade])

        # Exit game
        elif option.lower() == "e":
            player_state = {
                "name": "Player",
                "health": player.health,
                "strength": player.strength,
                "intelligence": player.intelligence,
                "gold": player.gold
            }
            save_game(player_state)

            break


main()


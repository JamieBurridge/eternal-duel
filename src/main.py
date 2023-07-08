from classes.Player import Player
from classes.Monster import Monster
from gameplay.fight import fight
from gameplay.reward import gold_reward
from gameplay.upgrade import upgrade_stat

from utils.options import main_menu_options, upgrade_options
from utils.game_states import load_game, save_game


def main():
    game_load_json = load_game()
    player = Player(game_load_json["name"], game_load_json["health"], game_load_json["strength"], game_load_json["intelligence"], game_load_json["gold"]) if game_load_json else Player("Player", 10, 10, 10, 20)

    while True:
        monster = Monster("Pixie", 10, 15, True, 20)

        option = None
        while option not in main_menu_options.keys():
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
            while stat_to_upgrade not in upgrade_options.keys():
                stat_to_upgrade = input("What stat would you like to upgrade? < [h]ealth, [s]trength, [i]ntelligence > ")

            upgrade_stat(player, upgrade_options[stat_to_upgrade])
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


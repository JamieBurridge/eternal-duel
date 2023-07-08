def upgrade_stat(player, stat):
    price_of_new_stat = player.get_stat(stat) * 1.5
    print(f"Price to upgrade {stat} is {price_of_new_stat} gold.")

    if player.gold < price_of_new_stat:
        print("You do not have enough gold.")
        return

    answer = None
    while answer not in ("y", "n"):
        answer = input(f"Would you like to upgrade your {stat}? < [y]es, [n]o > ")

    if answer == "y":
        player.gold -= price_of_new_stat
        player.set_stat(stat, player.get_stat(stat) + 2)
        print(f"You have upgraded your {stat} to {player.get_stat(stat)}!")

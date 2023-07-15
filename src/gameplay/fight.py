from time import sleep
from utils.options import fight_options

PRINT_SLEEP_TIME = 2


def fight(player, monster):
    player_max_health = player.health
    monster_max_health = monster.health

    participants = (player, monster)
    turn_index = 0

    print(f"A {monster.name} has appeared!! {monster.health} health.")

    while True:
        current_attacker = participants[turn_index]
        sleep(PRINT_SLEEP_TIME)

        if current_attacker.health <= 0:
            break

        print(f">>> {current_attacker.name}'s turn...")

        if current_attacker == player:
            option = None
            while option not in fight_options.keys():
                option = input("What do you want to do? < [f]ight, [m]agic > ")

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

    print(f"{participants[turn_index].name} has been DEFEATED!")

    # Restore player health
    player.health = player_max_health
    monster.health = monster_max_health

    # Return the loser
    return participants[turn_index]

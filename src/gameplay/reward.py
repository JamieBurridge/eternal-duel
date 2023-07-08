def gold_reward(player, defeated_monster):
    new_total_gold = player.gold + defeated_monster.gold_for_defeating

    print(f"GOLD: {player.gold} + {defeated_monster.gold_for_defeating} = {new_total_gold}")

    return new_total_gold

import random


def move(name_first_gamer1, name_second_gamer1, first1: int):
    if first1 % 2 == 0:
        return name_second_gamer1
    else:
        return name_first_gamer1


def bot_take_candies_random(candies_move_max_def):
    return random.randint(1, candies_move_max_def)


def clever_bot_take_candies(candies_def, candies_move_max_def):
    if candies_def % (candies_move_max_def + 1) == 0:
        return random.randint(1, candies_move_max_def)
    else:
        return candies_def % (candies_move_max_def + 1)




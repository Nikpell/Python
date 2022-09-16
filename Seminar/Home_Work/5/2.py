# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

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


# инициализация игры против бота
print('Вы хотите играть с компьютером или другом?')
choose = int(input('Если хотите играть с комрьютером введите 1, если с другом 2, с умным компьютером 3 '))

# # Инициализация двух игроков
if choose == 1 or choose == 3:
    name_first_gamer = 'Компьютер'
elif choose == 2:
    name_first_gamer = input('Игрок 1, введите Ваше имя: ')
name_second_gamer = input('Игрок 2, введите Ваше имя: ')
candies = int(input('Введите количество конфет: '))
candies_move_max = int(input('Введите максимальное количество конфет, которое можно взять  за ход: '))
# # Определение хода
first = random.randint(1, 2)
if first != 1:
    print(f'Первым начинает {name_second_gamer}')
else:
    print(f'Первым начинает {name_first_gamer}')

#     подсчет конфет
while candies > 0:
    gamer = move(name_first_gamer, name_second_gamer, first)
    if gamer == 'Компьютер':
        if choose == 3:
            candies_minus = clever_bot_take_candies(candies, candies_move_max)
        else:
            candies_minus = bot_take_candies_random(candies_move_max)
    else:
        candies_minus = int(
            input(f'{gamer}, сколько конфет вы хотите взять (не меньше 1 но не больше {candies_move_max})?: '))
    if candies_minus > candies_move_max or candies_minus < 1:
        print(f'Вы ошиблись, количество конфет не может быть меньше 1 и больше {candies_move_max}')
    elif (candies - candies_minus) < 0:
        print(f'Вы не можете взять конфет больше чем {candies}')
    else:
        candies -= candies_minus
        if candies == 0:
            print(f'Выиграл {gamer}, он забирает все конфеты!!!')
            break
        first += 1
        print(f'Игрок {gamer} взял {candies_minus} конфет. Осталось {candies} конфет')

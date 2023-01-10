from config import dp, bot
from aiogram import types
import game
import random

total = 20
max_take = 3


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    print(message.text)
    print('Hi')


@dp.message_handler(commands='game')
async def game_bot(message: types.Message):
    print(message.text)
    await bot.send_message(message.from_user.id, text='Введите количество конфет после команды /candies')


@dp.message_handler(commands='candies')
async def candies_bot(message: types.Message):
    global total
    if len(message.text.split()) > 1:
        total = int(message.text.split()[1])
    print(total)
    await bot.send_message(message.from_user.id, text='Введите максимальное количество конфет, которое можно взять '
                                                      ' за ход  после команды /max')


@dp.message_handler(commands='max')
async def max_take_bot(message: types.Message):
    global max_take
    if len(message.text.split()) > 1:
        max_take = int(message.text.split()[1])
    print(max_take)
    await bot.send_message(message.from_user.id, text='Если хотите ходить первым - наберите /first, '
                                                      'вторым /second, рандомно /rand ')


@dp.message_handler(commands='first')
async def first_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text='Сколько конфет возьмете?')


@dp.message_handler(commands='second')
async def second_bot(message: types.Message):
    global max_take
    global total
    bot_took = game.clever_bot_take_candies(total, max_take)
    if total - bot_took == 0:
        await bot.send_message(message.from_user.id,
                               text=f'Бот взял {bot_took} конфет и выиграл, он забирает все конфеты!!!')
    else:
        await bot.send_message(message.from_user.id, text=f'Bot взял'
                                                          f' {bot_took} конфет и на столе осталось'
                                                          f' {total - bot_took} конфет, Ваш ход')
    total -= bot_took


@dp.message_handler(commands='rand')
async def rand_bot(message: types.Message):
    first = random.randint(1, 2)
    if first != 1:
        await bot.send_message(message.from_user.id, text=f'Первым ходит {message.from_user.first_name}. '
                                                          f'Сколько конфет возьмете?')
    else:
        global max_take
        global total
        bot_took = game.clever_bot_take_candies(total, max_take)
        if total - bot_took == 0:
            await bot.send_message(message.from_user.id,
                                   text=f'Первым ходит бот. Бот взял {bot_took} конфет и выиграл, он забирает все конфеты!!!')
        else:
            await bot.send_message(message.from_user.id, text=f'Bot взял'
                                                              f' {bot_took} конфет и на столе осталось'
                                                              f' {total - bot_took} конфет, Ваш ход')
        total -= bot_took

@dp.message_handler()
async def all_bot(message: types.Message):
    global max_take
    global total
    if message.text.isdigit():
        if max_take >= int(message.text) and total - int(message.text) >= 0:
            total -= int(message.text)
            if total == 0:
                await bot.send_message(message.from_user.id,
                                       text=f'Выиграл {message.from_user.first_name}, он забирает все конфеты!!!')
            else:
                bot_took = game.clever_bot_take_candies(total, max_take)
                if total - bot_took == 0:
                    await bot.send_message(message.from_user.id,
                                           text=f'Бот взял {bot_took} конфет и выиграл, он забирает все конфеты!!!')
                else:
                    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, взял {message.text} '
                                                              f'конфет и на столе осталось {total} конфет, Bot взял'
                                                              f' {bot_took} конфет и на столе осталось'
                                                              f' {total - bot_took} конфет. Ваш ход')
                total -= bot_took
        else:
            await bot.send_message(message.from_user.id, text=f'нельзя брать конфет больше, чем есть на столе, '
                                                              f'меньше 0 или больше {max_take}')
    else:
        await bot.send_message(message.from_user.id, 'давай сначала конфеты разделим')

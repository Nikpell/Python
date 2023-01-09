from config import dp, bot
from aiogram import types
import random

total = 20


@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    print(message.text)
    print('Hi')


@dp.message_handler(commands='game')
async def game_bot(message: types.Message):
    print(message.text)
    await bot.send_message(message.from_user.id, text='Введите количество конфет:')
    # await bot.send_message(message.from_user.id, text='/candies')

@dp.message_handler()
async def all_bot(message: types.Message):

    if message.text.isdigit():
        if 4 > int(message.text) > 0:
            global total
            if total - int(message.text) > 0:
                total -= int(message.text)
                if total % (3 + 1) == 0:
                    bot_took = random.randint(1, 3)
                else:
                    bot_took = total % (3 + 1)
                    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, взял {message.text} '
                                                              f'конфет и на столе осталось {total} конфет, Bot взял'
                                                              f' {bot_took} конфет и на столе осталось'
                                                              f' {total - bot_took} конфет')
                total -= bot_took
            # elif #ToDo
            else:
                await bot.send_message(message.from_user.id, text='нельзя брать конфет больше, чем есть на столе')
        else:
            await bot.send_message(message.from_user.id, text='нельзя брать меньше 0 или больше 3 конфет')
    else:
        await bot.send_message(message.from_user.id, 'давай сначала конфеты разделим')
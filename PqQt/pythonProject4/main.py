import bot
from aiogram.utils import executor

if __name__ == '__main__':
    executor.start_polling(bot.dp, on_shutdown='shutdown')

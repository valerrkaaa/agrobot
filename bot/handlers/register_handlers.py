from bot.handlers import register_new_user_handlers
from bot import dp


def register_handlers():
    dp.register_message_handler(register_new_user_handlers.start, commands=['start'])
    dp.register_message_handler(register_new_user_handlers.stop, commands=['stop'])

    print('handlers started')

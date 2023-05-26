from aiogram import types
from bot import dp


def register_handlers():
    dp.register_message_handler(start, commands=['start'])


async def start(message: types.Message):
    print(message.from_user.id)

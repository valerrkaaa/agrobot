from aiogram import types
from bot import chat_id_list
from bot import dp


def register_handlers():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(stop, commands=['stop'])


async def start(message: types.Message):
    if message.chat.id not in chat_id_list:
        chat_id_list.append(message.from_user.id)
    await message.answer('Вы успешно подписались на рассылку!\nДля того, чтобы отписаться, введите: /stop')


async def stop(message: types.Message):
    chat_id_list.remove(message.chat.id)
    await message.answer('Вы успешно отписались от рассылки!\nДля того, чтобы снова подписаться, введите: /start')

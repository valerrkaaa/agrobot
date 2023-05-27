from aiogram import types
from bot import chat_id_list


async def start(message: types.Message):
    if message.chat.id not in chat_id_list:
        chat_id_list.append(message.from_user.id)
    await message.answer('Вы успешно подписались на рассылку!\nДля того, чтобы отписаться, введите: /stop')


async def stop(message: types.Message):
    chat_id_list.remove(message.chat.id)
    await message.answer('Вы успешно отписались от рассылки!\nДля того, чтобы снова подписаться, введите: /start')
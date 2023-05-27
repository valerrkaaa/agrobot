from aiogram.dispatcher import FSMContext
from api import apl_requests
from aiogram import types
from bot import states
from bot import bot


async def start(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать!\n'
                         'Для того, чтобы пользоваться нашим ботом, необходимо иметь '
                         'учётную запись на сайте .https://team-units.vercel.app и пройти регистрацию в этом боте')
    await set_email_state(message, state)


async def set_email_state(message: types.Message, state: FSMContext):
    await message.answer('Введите Вашу почту:')
    await state.set_state(states.Register.wait_email)


async def validate_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text.strip()

    await set_password_state(message, state)


async def set_password_state(message: types.Message, state: FSMContext):
    await message.answer('Введите Ваш пароль:\n'
                         '(сообщение будет удалено после авторизации)')
    await state.set_state(states.Register.wait_password)


async def validate_password(message: types.Message, state: FSMContext):
    await bot.delete_message(message.chat.id, message.message_id)

    async with state.proxy() as data:
        email = data.get('email')

    apl_requests.login(email, message.text.strip())


async def cancel_on_registration(message: types.Message):
    await message.answer('Регистрация отменена, для повторной регистрации введите /register')

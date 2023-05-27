from aiogram.dispatcher import FSMContext
from api import api_requests
from aiogram import types
from bot import states
from bot import bot


async def start(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать!\n'
                         'Для того, чтобы пользоваться нашим ботом, необходимо иметь '
                         'учётную запись на сайте: https://team-units.vercel.app и авторизоваться в этом боте')
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
    await bot.delete_message(message.chat.id, message.message_id - 1)

    async with state.proxy() as data:
        email = data.get('email')

    response = api_requests.login(email, message.text.strip())
    if response.get('status', '') == 'success':
        async with state.proxy() as data:
            data['user_id'] = response['user']['id']
            data['jwt'] = response['authorisation']['token']

        await message.answer('Авторизация прошла успешно!\n'
                             'Чтобы посмотреть список продуктов в Вашей корзине, введите /cart')
        await state.set_state(states.Main.default_state)
    else:
        await message.answer('Неверный логин или пароль!')
        await set_email_state(message, state)


async def cancel_on_registration(message: types.Message):
    await message.answer('Авторизация отменена, для повторной попытки введите /login')

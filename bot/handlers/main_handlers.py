from bot.handlers import register_new_user_handlers
from aiogram.dispatcher import FSMContext
from aiogram import types
from bot import keyboards


async def send_product_list(message: types.Message, state: FSMContext):
    if message.text.lower() == 'Показать корзину':
        await message.answer('Ваша корзина:', reply_markup=keyboards.generate_cart_keyboard({"id": 1, "price": 500}))
    await message.answer('Ваша корзина: пуста', reply_markup=keyboards.default_keyboard())


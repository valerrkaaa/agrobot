from aiogram.dispatcher import FSMContext
from aiogram import types
from api import api_requests
from bot import states


async def set_product_name_state(message: types.Message, state: FSMContext):
    await message.answer('Введите название продукта:')
    await state.set_state(states.NewProduct.wait_product_name)


async def validate_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_product'] = {'name': message.text.strip()}
    await set_product_description_state(message, state)


async def set_product_description_state(message: types.Message, state: FSMContext):
    # Отмена
    await message.answer('Введите описание товара:')
    await state.set_state(states.NewProduct.wait_description)


async def validate_product_description(message: types.Message, state: FSMContext):
    description = '' if message.text == 'Отмена' else message.text
    async with state.proxy() as data:
        data['new_product']['description'] = description

    await set_product_photo_state(message, state)


async def set_product_photo_state(message: types.Message, state: FSMContext):
    await message.answer('Загрузите фотографию продукта:')
    await state.set_state(states.NewProduct.wait_image)


async def validate_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_product']['photo'] = None  # TODO

    await set_product_price_state(message, state)


async def skip_validate_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_product']['photo'] = None
    await set_product_price_state(message, state)


async def set_product_price_state(message: types.Message, state: FSMContext):
    await message.answer('Введите цену продукта:')
    await state.set_state(states.NewProduct.wait_price)


async def validate_product_price(message: types.Message, state: FSMContext):
    try:
        price = float(message.text)
        async with state.proxy() as data:
            data['new_product']['price'] = price

        response = api_requests.create_product(
            jwt=data['jwt'],
            name=data['new_product']['name'],
            description=data['new_product']['description'],
            image=data['new_product']['image'],
            price=data['new_product']['price'],
        )
        if response.get('status', '') == 'success':
            await message.answer('Товар размещён успешно')
        else:
            await message.answer('Не удалось опубликовать товар!')

    except ValueError:
        await message.answer('Необходимо ввести число!')


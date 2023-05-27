from aiogram.dispatcher import FSMContext
from aiogram import types
from bot import keyboards
from api import api_requests
from bot import bot


async def show_product_cart(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        jwt = data['jwt']
    response = api_requests.get_product_card(jwt)

    photo = 'AgACAgIAAxkBAAMNZHHIN1KU6pqQiwYi01OiPODQ4N0AAuzLMRu4pIhLQnr-1TH-KDIBAAMCAANzAAMvBA'

    if str(response.get('success', '')) == '1':
        for item in response['data']['items']:
            keyboard = keyboards.generate_cart_keyboard({})
            if item['product']['description']:
                description = '\nОписание:\n' + item['product']['description'] + '\n'
            else:
                description = ''

            # await bot.send_photo(chat_id=message.chat.id, photo=photo)
            # await message.answer(f"{item['product']['name']}\n{description}\n"
            #                      f"Цена: {item['product']['price']}")
            await bot.send_photo(chat_id=message.chat.id, photo=photo,
                                 caption=f"{item['product']['name']}\n{description}\nЦена: {item['product']['price']}",
                                 reply_markup=keyboard)
            # TODO inline написать фермеру (item['product']['farmer_id'])
    else:
        await message.answer('Во время запроса произошла ошибка :(')


async def get_photo(msg: types.Message):
    document_id = msg.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'file_path: {file_info.file_path}')
    print(f'file_size: {file_info.file_size}')
    print(f'file_unique_id: {file_info.file_unique_id}')
    await bot.send_photo(chat_id=msg.chat.id, photo=file_info.file_id)

# async def show_product_list(message: types.Message, state: FSMContext):
#     response = api_requests.get_product_list()
#
#     if str(response.get('success', '')) == '1':
#
#     else:
#         await message.answer('Во время запроса произошла ошибка :(')

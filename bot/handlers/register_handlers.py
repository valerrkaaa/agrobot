import aiogram.types

from bot.handlers import register_new_user_handlers as register
from bot.handlers import main_handlers as main
from bot.handlers import farmer_handlers as new_product
from bot import dp
from bot import states


def register_handlers():
    # dev
    # dp.register_message_handler(main.get_photo, content_types=['photo'])

    # login
    dp.register_message_handler(register.start, commands=['start'])
    dp.register_message_handler(register.set_email_state, commands=['login'])
    dp.register_message_handler(register.validate_email, state=states.Register.wait_email)
    dp.register_message_handler(register.validate_password, state=states.Register.wait_password)
    dp.register_message_handler(register.cancel_on_registration, text='Отмена', state=[states.Register.wait_password])

    # main
    dp.register_message_handler(show_help, commands=['help'])
    dp.register_message_handler(main.show_product_cart, commands=['cart'], state=[states.Main.default_state])

    # new product
    dp.register_message_handler(new_product.set_product_name_state, commands=['create'],
                                state=[states.Main.default_state])
    dp.register_message_handler(new_product.validate_product_name,
                                state=[states.NewProduct.wait_product_name])
    dp.register_message_handler(new_product.validate_product_description,
                                state=[states.NewProduct.wait_description])
    dp.register_message_handler(new_product.validate_product_photo,
                                state=[states.NewProduct.wait_image])
    dp.register_message_handler(new_product.skip_validate_product_photo, text=['Отмена'],
                                state=[states.NewProduct.wait_image])
    dp.register_message_handler(new_product.validate_product_price,
                                state=[states.NewProduct.wait_price])


async def show_help(message: aiogram.types.Message):
    await message.answer('/cart - список товаров в корзине"\n\n'
                         'Для фермеров:\n/create - загрузить новый товар на продажу')

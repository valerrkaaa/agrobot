from bot.handlers import register_new_user_handlers as register
from bot.handlers import main_handlers as main
from bot import dp
from bot import states


def register_handlers():
    # dev
    dp.register_message_handler(main.get_photo, content_types=['photo'])

    # login
    dp.register_message_handler(register.start, commands=['start'])
    dp.register_message_handler(register.set_email_state, commands=['login'])
    dp.register_message_handler(register.validate_email, state=states.Register.wait_email)
    dp.register_message_handler(register.validate_password, state=states.Register.wait_password)
    dp.register_message_handler(register.cancel_on_registration, text='Отмена', state=[states.Register.wait_password])

    # main
    dp.register_message_handler(main.show_product_cart, commands=['cart'], state=[states.Main.default_state])

from bot.handlers import register_new_user_handlers as register
from bot import dp
from bot import states


def register_handlers():
    dp.register_message_handler(register.start, commands=['start'])
    dp.register_message_handler(register.set_email_state, commands=['register'])
    dp.register_message_handler(register.validate_email, state=states.Register.wait_email)
    dp.register_message_handler(register.validate_password, state=states.Register.wait_password)
    dp.register_message_handler(register.cancel_on_registration, text='Отмена', state=[states.Register.wait_password])

    print('handlers started')

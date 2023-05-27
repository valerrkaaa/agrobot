from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    wait_email = State()
    wait_password = State()

from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    wait_email = State()
    wait_password = State()


class Main(StatesGroup):
    default_state = State()


class NewProduct(StatesGroup):
    wait_product_name = State()
    wait_description = State()
    wait_image = State()
    wait_price = State()

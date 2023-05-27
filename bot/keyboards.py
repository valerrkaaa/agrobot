from aiogram import types


def generate_cancel_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Отмена'))
    return keyboard


def generate_cart_keyboard(items):
    return None

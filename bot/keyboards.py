from aiogram import types
from __init__ import *


def generate_cancel_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Отмена'))
    return keyboard


# async def generate_contact_keyboard():
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(types.KeyboardButton('Отправить номер телефона', request_contact=True))
#     keyboard.add(types.KeyboardButton('Отмена'))
#     return keyboard


def generate_yes_or_no_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Да'))
    keyboard.add(types.KeyboardButton('Нет'))
    return keyboard


def generate_cart_keyboard(lines: dict):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(types.InlineKeyboardButton(text='Показать корзину',
                                                   callback_data="show_cart"))
    for k, v in lines.items():
        text = lines[k] + " Цена:" + lines["price"]
        keyboard_markup.add(types.InlineKeyboardMarkup(text=text, callback_data=request_callback_data.new(
            type=k)))
    return keyboard_markup


def default_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(text='Показать корзину',
                                                   callback_data="show_cart"))
    return keyboard

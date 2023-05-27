from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram
import tokens
from aiogram.utils.callback_data import CallbackData


request_full_callback_list = CallbackData('callback_data', 'type', 'request_id')
request_callback_data = CallbackData('callback_data', 'type')

bot = aiogram.Bot(token=tokens.tg_bot_token)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

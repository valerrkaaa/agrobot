from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram
import tokens

bot = aiogram.Bot(token=tokens.tg_bot_token)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

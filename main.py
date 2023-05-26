from aiogram.utils import executor
from bot.handlers import register_new_user_handler
from bot import dp


def main():
    # запуск бот хэндлеров
    register_new_user_handler.register_handlers()

    # второй поток: запуск sl

    # запуск бота
    executor.start_polling(dp)


if __name__ == '__main__':
    main()

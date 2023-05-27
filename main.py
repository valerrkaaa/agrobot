from bot.handlers import register_handlers
from aiogram.utils import executor
from bot import dp


def main():
    # запуск бот хэндлеров
    register_handlers.register_handlers()

    print('bot started')

    # запуск бота
    executor.start_polling(dp)


if __name__ == '__main__':
    main()

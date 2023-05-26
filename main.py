from bot.handlers import register_new_user_handler
from socketListeners import socketListener
from aiogram.utils import executor
from bot import dp
import threading


def main():
    # запуск бот хэндлеров
    register_new_user_handler.register_handlers()

    # второй поток: запуск socket listener
    socket_listener_thread = threading.Thread(target=socketListener.start_async_listener)
    socket_listener_thread.start()

    # запуск бота
    executor.start_polling(dp)


if __name__ == '__main__':
    main()

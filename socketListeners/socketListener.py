from tokens import websocket_url
from bot import chat_id_list, bot
import websockets
import asyncio


async def socket_handler(web_socket: websockets.WebSocketClientProtocol) -> None:
    async for message in web_socket:
        for chat_id in chat_id_list:
            # TODO обработка json
            bot.send_message(chat_id, message)


async def start_listen_socket() -> None:
    async with websockets.connect(websocket_url) as web_socket:
        await socket_handler(web_socket)


def start_async_listener():
    asyncio.run(start_listen_socket())

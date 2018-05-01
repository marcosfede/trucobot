import asyncio
import websockets
import argparse
import json
from fedebot import FedeBot
from handlers import MessageHandler


async def serve(websocket, path):
    bot = FedeBot()
    handler = MessageHandler(bot, websocket)
    async for message in websocket:
        message = json.loads(message)
        print(message)
        await getattr(handler, message["mensaje"])(message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start the trucobot')
    parser.add_argument('--port',  default=3000, help='port to listen in')
    args = parser.parse_args()

    start_server = websockets.serve(serve, 'localhost', args.port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

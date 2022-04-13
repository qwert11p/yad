import logging
import os

from aiogram import Bot, Dispatcher, types, executor, filters

API_TOKEN = os.environ['API_TOKEN']
PACK_NAME1 = os.environ['PACK_NAME1']

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)
    
@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def handler(msg: types.Message):
    if msg.sticker.set_name != PACK_NAME1:
        await msg.delete()


if __name__ == '__main__':
    executor.start_polling(dp)
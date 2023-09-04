from config.config import logging, bot_token

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart


dp = Dispatcher()
bot = Bot(bot_token)


@dp.message(CommandStart())
async def command_start_handler(message):
    await message.answer(f"Hello, {message.from_user.full_name}!")


@dp.message(F.text)
async def echo_handler(message):
    await message.answer_photo(message.text)


@dp.message(F.photo)
async def photo_handler(message):

    await message.answer(message.photo[0].file_id)


logging.info("Application started")
dp.run_polling(bot)

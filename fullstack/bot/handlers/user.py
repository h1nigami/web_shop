from loader import dp, bot, types
from aiogram import F, Router
from aiogram.filters import Command
from data import config, db

import logging

logging.basicConfig(level=logging.INFO)

router = Router()

@dp.message(Command(commands=['start']))
async def startup(message:types.Message):
    await db.create_user(tg_id=message.from_user.id, username=message.from_user.username)
    photo = types.FSInputFile(path=r'fullstack/bot/src/img/магазин.jpg')
    await bot.send_photo(photo=photo, caption='Добро пожаловать в наш магазин!', chat_id=message.from_user.id)
    
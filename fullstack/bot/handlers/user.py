from loader import dp, bot, types
from aiogram import F, Router
from aiogram.filters import Command
from data import config, db

from aiogram.fsm import FSMContext

import logging

logging.basicConfig(level=logging.INFO)

router = Router()

@dp.message(Command(commands=['start']))
async def startup(message:types.Message):
    await db.create_user(tg_id=message.from_user.id, username=message.from_user.username)
    await bot.send_photo(chat_id=message.from_user.id, photo=open(r'src/магазин.jpg'), caption='Добро пожаловать в магазин')
    
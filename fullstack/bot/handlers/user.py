from loader import dp, bot, types
from aiogram import Router, F
from aiogram.filters import Command
from data import config, db, bot_db

from aiogram.enums.parse_mode import ParseMode

from keyboard import *

import logging

logging.basicConfig(level=logging.INFO)

router = Router()

@dp.callback_query(F.data == 'main_menu')
@dp.message(Command(commands=['start']))
async def startup(message:types.Message):
    await bot_db.create_user(tg_id=message.from_user.id, username=message.from_user.username)
    photo = types.FSInputFile(path=r'fullstack/bot/src/img/магазин.jpg')
    await bot.send_photo(photo=photo, 
                        caption='<b>Добро пожаловать в наш магазин!</b>\nВыберите пункт меню:', 
                        chat_id=message.from_user.id, 
                        parse_mode=ParseMode.HTML,
                        reply_markup=main_menu())
    
@dp.callback_query(F.data == 'catalog')
async def catalog(callback: types.callback_query):
    await bot.send_message(chat_id=callback.from_user.id, text='Выберите категорию товара', reply_markup=catalog_menu())
    
@dp.callback_query(F.data == 'profile')
async def about(callback: types.callback_query):
    balance = await bot_db.get_user_balance(tg_id=callback.from_user.id)
    discount = await bot_db.get_user_discard(tg_id=callback.from_user.id)
    _ = await bot_db.get_order_history(tg_id=callback.from_user.id)
    if ':' in _:
        orders_count = _.count(':') + 1
    elif _ == '':
        orders_count = 0
    else:
        orders_count = 1
    registration = await bot_db.get_user_registration_date(tg_id=callback.from_user.id)
    return await bot.send_message(chat_id=callback.from_user.id,
                                  text=f'ID: {callback.from_user.id}\nБаланс: {balance}\nПерсональная скидка: {discount}\nВсего покупок: {orders_count}\nРегистрация: {registration}',
                                  reply_markup=about_menu())
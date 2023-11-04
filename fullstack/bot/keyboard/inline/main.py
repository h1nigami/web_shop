from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import bot_db

def main_menu():
    keyboard = InlineKeyboardBuilder()
    #ключи - названия кнопок, значение - коллбек дата
    buttons = {
        'Каталог товаров': 'catalog',
        'Каталог WebApp': 'webapp',
        'Корзина': 'cart',
        'Мой профиль': 'profile',
    }
    for key, value in buttons.items():
        keyboard.button(text=key, callback_data=value)
    return keyboard.as_markup()

def catalog_menu():
    categories = await bot_db.get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in categories:
        keyboard.button(text=category, callback_data=category)
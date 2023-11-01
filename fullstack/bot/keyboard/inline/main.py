from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu():
    keyboard = InlineKeyboardBuilder()
    buttons = {
        'Каталог товаров': 'catalog',
        'Каталог WebApp': 'webapp',
        'Корзина': 'cart',
        'Мой профиль': 'profile',
    }
    for key, value in buttons.items():
        keyboard.button(text=key, callback_data=value)
    return keyboard.as_markup()
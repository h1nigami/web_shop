from aiogram.filters.state import State, StatesGroup

class ProductOrder(StatesGroup):
    category = State()
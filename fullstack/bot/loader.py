from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types

from data import config

bot = Bot(token=config.get_token(), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
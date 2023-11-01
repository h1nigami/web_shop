from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types

from data import config

bot = Bot(token=config.get_token())
dp = Dispatcher(storage=MemoryStorage())
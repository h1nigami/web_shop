from loader import dp, bot, types
from aiogram import F, Router
from data import config, db

from aiogram.fsm import FSMContext

import logging

logging.basicConfig(level=logging.INFO)

router = Router()
from handlers import dp, bot
import asyncio
from data import db
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await db.create_tables()
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
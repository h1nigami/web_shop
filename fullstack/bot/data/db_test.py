import asyncio
from database_settings import bot_db

async def main():
    orders = await bot_db.get_order_history(932343818)
    result = '123:321'
    try:
        assert orders == result
        print(f'{orders} == {result}')
    except:
        print(f'{orders} != {result}')
    
if __name__ == '__main__':
    asyncio.run(main())
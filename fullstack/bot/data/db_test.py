import asyncio
from database_settings import bot_db

async def order_test():
    orders = await bot_db.get_order_history(932343818)
    result = '123:321'
    try:
        assert orders == result
        print(f'Test passed\n{orders} == {result}')
    except AssertionError:
        print(f'Test failed\n{orders} != {result}')
        
async def categories_test():
    categories = await bot_db.get_categories()
    result = ['еда', 'одежда']
    try:
        assert categories == result
        print(f'Test passed\n{categories} == {result}')
    except AssertionError:
        print(f'Test failed\n{categories} != {result}')
    
if __name__ == '__main__':
    asyncio.run(order_test())
    asyncio.run(categories_test())
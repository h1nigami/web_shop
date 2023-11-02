import aiosqlite
import datetime

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
    #создание таблиц    
    async def create_tables(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT,
                balance INTEGER,
                discard INTEGER,
                register_date TEXT,
                orders TEXT DEFAULT NULL)""")
            await db.execute("""CREATE TABLE IF NOT EXISTS products(
                name TEXT,
                cost INTEGER,
                category TEXT)""")
            await db.commit()
    
    #работа с юзерами        
    async def create_user(self, tg_id, username):
        try:
            async with aiosqlite.connect(self.db_name) as db:
                await db.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", (tg_id, username, 0, 0, str(datetime.datetime.now()), None))
                await db.commit()
        except aiosqlite.IntegrityError:
            pass
    
    async def get_user(self, username):
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute("SELECT * FROM users WHERE username = ?", (username,)) as cursor:
                user = await cursor.fetchone()
                return user
    #работа с ботами (только в основной бд)        
    async def get_token(self, owner_id):
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute("SELECT token FROM backend_api_bots WHERE owner_id = ?", (owner_id,)) as cursor:
                token = await cursor.fetchone()
                return token
            
    #работа с ордерами //TODO
    async def get_order_history(self, tg_id):
        '''
        возвращает список заказов пользователя в формате заказ:заказ1:заказ2 для обработки используй split(':')
        '''
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute("SELECT orders FROM users WHERE id = ?", (tg_id,)) as cursor:
                order = await cursor.fetchone()
                return order
            
    async def create_order(self, tg_id:int, order:str):
        pre_orders = await self.get_order_history(tg_id)
        if pre_orders is None:
            order = order
        else:
            order = pre_orders + ':' + order
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(F"UPDATE users SET orders = {order} WHERE id = {tg_id}")
            await db.commit()
            
    #работа с категориями
    async def get_categories(self):
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute("SELECT DISTINCT category FROM products") as cursor:
                categories = await cursor.fetchall()
                return categories
            
db = DataBase(r'fullstack\db.sqlite3')
bot_db = DataBase(r'fullstack/bot/db.sqlite3')
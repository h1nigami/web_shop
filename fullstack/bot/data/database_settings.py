import aiosqlite

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
    #создание таблиц    
    async def create_tables(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT)""")
            await db.execute("""CREATE TABLE IF NOT EXISTS products(
                name TEXT,
                cost INTEGER)""")
            await db.commit()
    
    #работа с юзерами        
    async def create_user(self, tg_id, username):
        try:
            async with aiosqlite.connect(self.db_name) as db:
                await db.execute("INSERT INTO users VALUES (?, ?)", (tg_id, username))
                await db.commit()
        except aiosqlite.IntegrityError:
            pass
    
    async def get_user(self, username):
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute("SELECT * FROM users WHERE username = ?", (username,)) as cursor:
                user = await cursor.fetchone()
                return user
    #работа с ботами        
    async def get_token(self, owner_id):
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute("SELECT token FROM backend_api_bots WHERE owner_id = ?", (owner_id,)) as cursor:
                token = await cursor.fetchone()
                return token
            
db = DataBase(r'fullstack\db.sqlite3')
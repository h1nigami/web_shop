import aiosqlite

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        
    async def create_tables(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT,)""")
            await db.execute("""CREATE TABLE IF NOT EXISTS products(
                name TEXT,
                cost INTEGER,)""")
            await db.commit()
            
    async def create_user(self, tg_id, username):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("INSERT INTO users VALUES (?, ?)", (tg_id, username))
            await db.commit()
    
    async def get_user(self, username):
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute("SELECT * FROM users WHERE username = ?", (username,)) as cursor:
                user = await cursor.fetchone()
                return user
            
db = DataBase(r'fullstack\db.sqlite3')
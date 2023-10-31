import aiosqlite

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        
    async def create_tables(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,)""")
            await db.execute("""CREATE TABLE IF NOT EXISTS products(
                name TEXT,
                cost INTEGER,)""")
import random
import sqlite3

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()
    if db:
        print('DB connected')
        db.execute("CREATE TABLE IF NOT EXISTS mentorsGeeks"
               "(id INTEGER PRIMARY KEY, "
               "name VARCHAR (50),"
               "position VARCHAR (40),"
               "age INTEGER,"
               "potok INTEGER)")
        db.commit()
async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT OR IGNORE INTO mentorsGeeks VALUES (?, ?, ?, ?, ?)",
                      tuple(data.values()))
        db.commit()
async def sql_command_random():
    result = cursor.execute("SELECT * FROM mentorsGeeks").fetchall()
    random_user = random.choice(result)
    return random_user
async def sql_command_all():
    return cursor.execute("SELECT * FROM mentorsGeeks").fetchall()
async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentorsGeeks WHERE id = ?", (id,))
    db.commit()

sql_create()

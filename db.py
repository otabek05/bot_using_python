import sqlite3
def create_user_table():
    db=sqlite3.connect("db.db")
    print(db)
    cursor=db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NPT NULL UNIQUE,
        username VARCHAR(200),
        first_name VARCHAR(200),
        last_name VARCHAR(200),
        full_name VARCHAR(200)
    )""")
    db.commit()
    db.close()

create_user_table()



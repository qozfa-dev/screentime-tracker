import sqlite3

# Connects to the SQLite database


def connect_db():
    conn = sqlite3.connect('screen_time.db')
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS screen_time (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT NOT NULL,
                   app TEXT NOT NULL,
                   category TEXT NOT NULL,
                   minutes INTEGER NOT NULL)
                   ''')
    conn.commit()
    conn.close()


create_table()

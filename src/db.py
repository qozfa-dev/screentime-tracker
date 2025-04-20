import sqlite3


def connect_db():
    conn = sqlite3.connect('screen_time.db')
    return conn

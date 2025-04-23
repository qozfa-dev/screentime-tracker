from db import connect_db
import datetime


def log_usage(app, category, minutes):
    conn = connect_db()
    cursor = conn.cursor()
    # Get the current date
    date = datetime.date.today().isoformat()

    # Inserts values into the screen_time database
    cursor.execute('''
                   INSERT INTO screen_time (date, app, category, minutes
                   VALUES (?, ?, ?, ?)
                   ''', (date, app, category, minutes))

    conn.commit()
    conn.close()

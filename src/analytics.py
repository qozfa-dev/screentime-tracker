from db import connect_db
import datetime


def get_total_usage_today():
    today = datetime.date.today().isoformat()
    conn = connect_db
    cursor = conn.cursor()

    # SQL query to get the total minutes of screentime today
    cursor.execute(
        "SELECT SUM(minutes) FROM screen_time WHERE date = ?", (today,))
    result = cursor.fetchone()[0]  # Returns the first row of the result
    return result or 0


def get_top_apps_today(n=3):
    today = datetime.date.today().isoformat()
    conn = connect_db
    cursor = conn.cursor()

    cursor.execute('''
                   SELECT app, SUM(minutes) as total 
                   FROM screen_time
                   WHERE date = ?
                   GROUP BY app 
                   ORDER BY total DESC LIMIT ?
                   ''', (today, n))
    return cursor.fetchall()  # Returns all the rows from the result of the query

import sqlite3


def execute_sql(query):
    conn = sqlite3.connect("database/hospital.db")

    cursor = conn.cursor()
    cursor.execute(query)

    results = cursor.fetchall()

    conn.close()

    return results
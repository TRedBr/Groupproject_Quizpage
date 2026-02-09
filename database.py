import sqlite3

def initialise_database():
    conn = sqlite3.connect("datadir/datadirectory.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER,
        name TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
    id INTEGER,
    Quizname TEXT,
    )""")
    cursor.execute("SELECT * FROM users")
    for user in cursor.fetchall():
        print(user)
    conn.execute("SELECT * FROM quizzes")
    for quiz in cursor.fetchall():
        print(quiz)
    conn.close()


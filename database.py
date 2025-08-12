import sqlite3

def get_connection():
    return sqlite3.connect("agent.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()
    conn.close()

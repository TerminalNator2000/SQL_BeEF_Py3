# core/db_logger.py
import sqlite3
from datetime import datetime

def log_action(tool, message):
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY,
                        tool TEXT,
                        message TEXT,
                        timestamp TEXT
                    )""")
    timestamp = datetime.now().isoformat()
    cursor.execute("INSERT INTO logs (tool, message, timestamp) VALUES (?, ?, ?)", (tool, message, timestamp))
    conn.commit()
    conn.close()

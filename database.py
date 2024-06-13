import sqlite3

def get_connection():
    conn = sqlite3.connect('part_manager.db')
    conn.row_factory = sqlite3.Row
    return conn

CONN = get_connection()
CURSOR = CONN.cursor()

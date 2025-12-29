import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    db_path = os.getenv('DATABASE_URL', 'books.db')
    return sqlite3.connect(db_path)
def init_database():
    """Initialize the database with tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create authors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    # Create books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            genre TEXT,
            status TEXT DEFAULT 'unread',
            date_added TEXT,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database tables created successfully!")

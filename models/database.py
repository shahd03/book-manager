import sqlite3
import os
from config.settings import settings

def get_connection():
    """Get a database connection"""
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(settings.DATABASE_URL.replace("sqlite:///", ""))

def init_db():
    """Initialize database with tables"""
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
            author_id INTEGER,
            genre TEXT,
            status TEXT DEFAULT 'unread',
            date_added TEXT,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")
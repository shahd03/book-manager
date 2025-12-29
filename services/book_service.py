from models.database import get_connection
from datetime import date

class BookService:
    def __init__(self):
        self.conn = None
    
    def connect(self):
        self.conn = get_connection()
        return self.conn
    
    def close(self):
        if self.conn:
            self.conn.close()
    
    def add_book(self, title, author_name, genre):
        """Add a new book to the database"""
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            # 1. Add author if not exists
            cursor.execute("SELECT id FROM authors WHERE name = ?", (author_name,))
            author = cursor.fetchone()
            
            if not author:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (author_name,))
                author_id = cursor.lastrowid
            else:
                author_id = author[0]
            
            # 2. Add the book
            cursor.execute('''
                INSERT INTO books (title, author_id, genre, status, date_added)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, author_id, genre, 'unread', str(date.today())))
            
            conn.commit()
            print(f"Book '{title}' added successfully!")
            return True
            
        except Exception as e:
            print(f"Error adding book: {e}")
            return False
        finally:
            conn.close()

    def get_all_books(self):
        """Get all books with author names"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT b.id, b.title, a.name, b.genre, b.status, b.date_added
            FROM books b
            JOIN authors a ON b.author_id = a.id
            ORDER BY b.id
        ''')
        
        books = cursor.fetchall()
        conn.close()
        return books

    def update_book_status(self, book_id, new_status):
        """Update the reading status of a book"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE books SET status = ? WHERE id = ?", (new_status, book_id))
        
        if cursor.rowcount > 0:
            print(f"Book status updated to '{new_status}'")
            conn.commit()
            result = True
        else:
            print("Book not found!")
            result = False
        
        conn.close()
        return result

    def search_books(self, author=None, genre=None, status=None):
        """Search books with filters"""
        conn = get_connection()
        cursor = conn.cursor()
        
        query = '''
            SELECT b.id, b.title, a.name, b.genre, b.status
            FROM books b
            JOIN authors a ON b.author_id = a.id
            WHERE 1=1
        '''
        params = []
        
        if author:
            query += " AND a.name LIKE ?"
            params.append(f"%{author}%")
        
        if genre:
            query += " AND b.genre LIKE ?"
            params.append(f"%{genre}%")
        
        if status:
            query += " AND b.status = ?"
            params.append(status)
        
        cursor.execute(query, params)
        books = cursor.fetchall()
        conn.close()
        return books

    def get_statistics(self):
        """Get collection statistics"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM books")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'read'")
        read = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'reading'")
        reading = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'unread'")
        unread = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total': total,
            'read': read,
            'reading': reading,
            'unread': unread,
            'completion_rate': (read / total * 100) if total > 0 else 0
        }
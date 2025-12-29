import pandas as pd
from models.database import get_connection

def generate_csv_report():
    """Generate CSV report of all books"""
    conn = get_connection()
    
    # Read data directly into pandas
    query = '''
        SELECT b.id, b.title, a.name as author, b.genre, b.status, b.date_added
        FROM books b
        JOIN authors a ON b.author_id = a.id
    '''
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if not df.empty:
        df.to_csv('book_collection.csv', index=False)
        print("CSV report generated: book_collection.csv")
        return True
    else:
        print("No books to report")
        return False

def generate_excel_report():
    """Generate Excel report of all books"""
    conn = get_connection()
    
    query = '''
        SELECT b.id, b.title, a.name as author, b.genre, b.status, b.date_added
        FROM books b
        JOIN authors a ON b.author_id = a.id
    '''
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if not df.empty:
        df.to_excel('book_collection.xlsx', index=False, engine='openpyxl')
        print("Excel report generated: book_collection.xlsx")
        return True
    else:
        print("No books to report")
        return False

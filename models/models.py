class Book:
    def __init__(self, title, author_id, genre, year, book_id=None):
        self.book_id = book_id
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.year = year
    
    def __repr__(self):
        return f"Book('{self.title}', {self.year})"

class Author:
    def __init__(self, name, author_id=None):
        self.author_id = author_id
        self.name = name
    
    def __repr__(self):
        return f"Author('{self.name}')"

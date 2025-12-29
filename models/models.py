def init_db():
    """Initialize the database"""
    from models.database import init_database
    init_database()
    print("Database initialized!")
import sys
from services.book_service import BookService
from services.report_service import ReportService
from models.models import init_db

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--init":
        init_db()
        print("Database initialized successfully!")
        return
    
    # Interactive mode
    service = BookService()
    report_service = ReportService()
    
    while True:
        print("\n" + "="*50)
        print("PERSONAL BOOK COLLECTION MANAGER")
        print("="*50)
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search books")
        print("4. Update book status")
        print("5. View statistics")
        print("6. Generate report")
        print("7. Exit")
        print("-"*50)
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == "1":
            print("\nAdd New Book")
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            
            service.add_book(title, author, genre)
        
        elif choice == "2":
            books = service.get_all_books()
            print("\n" + "-"*80)
            print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Genre':<15} {'Status':<10}")
            print("-"*80)
            for book in books:
                print(f"{book[0]:<5} {book[1][:28]:<30} {book[2][:18]:<20} {book[3][:13]:<15} {book[4]:<10}")
        
        elif choice == "3":
            print("\nSearch Books")
            print("Leave field empty to skip")
            author = input("Author: ")
            genre = input("Genre: ")
            status = input("Status (read/reading/unread): ")
            
            books = service.search_books(
                author=author if author else None,
                genre=genre if genre else None,
                status=status if status else None
            )
            
            print(f"\nFound {len(books)} books:")
            for book in books:
                print(f"  - {book[1]} by {book[2]} ({book[4]})")
        
        elif choice == "4":
            try:
                book_id = int(input("Book ID to update: "))
                status = input("New status (read/reading/unread): ")
                if service.update_book_status(book_id, status):
                    print("Status updated successfully!")
                else:
                    print("Book not found!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "5":
            stats = service.get_statistics()
            print("\nCollection Statistics")
            print(f"Total books: {stats['total']}")
            print(f"Read: {stats['read']}")
            print(f"Currently reading: {stats['reading']}")
            print(f"Unread: {stats['unread']}")
            print(f"Completion rate: {stats['completion_rate']:.1f}%")
        
        elif choice == "6":
            format = input("Report format (csv/excel): ").lower()
            filename = report_service.generate_reading_report(format)
            print(f"Report generated: {filename}")
        
        elif choice == "7":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
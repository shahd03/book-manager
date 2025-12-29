import csv
import os
from datetime import datetime
from services.book_service import BookService

class ReportService:
    def __init__(self):
        self.book_service = BookService()
    
    def generate_collection_report(self, format='csv'):
        """Generate a report of all books"""
        books = self.book_service.get_all_books()
        
        if not books:
            print("No books found to generate report!")
            return None
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if format.lower() == 'csv':
            filename = f"collection_report_{timestamp}.csv"
            try:
                with open(filename, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    # Write header
                    writer.writerow(['ID', 'Title', 'Author', 'Genre', 'Status', 'Date Added'])
                    # Write data
                    for book in books:
                        writer.writerow(book)
                print(f"✓ Collection report saved as '{filename}'")
                print(f"  Location: {os.path.abspath(filename)}")
                print(f"  Number of books exported: {len(books)}")
                return filename
            except Exception as e:
                print(f"✗ Error generating CSV report: {e}")
                return None
                
        elif format.lower() == 'excel':
            try:
                # Try to import pandas for Excel support
                import pandas as pd
                
                # Convert to DataFrame
                df = pd.DataFrame(books, columns=['ID', 'Title', 'Author', 'Genre', 'Status', 'Date Added'])
                
                filename = f"collection_report_{timestamp}.xlsx"
                df.to_excel(filename, index=False)
                
                print(f"✓ Excel report saved as '{filename}'")
                print(f"  Location: {os.path.abspath(filename)}")
                print(f"  Number of books exported: {len(books)}")
                return filename
                
            except ImportError:
                print("  Pandas library not installed. Excel export requires 'pandas' package.")
                print("  Install it with: pip install pandas openpyxl")
                print("  Falling back to CSV format...")
                return self.generate_collection_report('csv')
            except Exception as e:
                print(f" Error generating Excel report: {e}")
                return None
        else:
            print(f"Unsupported format: {format}. Use 'csv' or 'excel'.")
            return None
    
    def generate_reading_report(self, format='csv'):
        """Generate a report of reading statistics"""
        stats = self.book_service.get_statistics()
        
        if stats['total'] == 0:
            print("No books found to generate statistics!")
            return None
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if format.lower() == 'csv':
            filename = f"reading_report_{timestamp}.csv"
            try:
                with open(filename, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    # Write header
                    writer.writerow(['Statistic', 'Value'])
                    # Write data
                    writer.writerow(['Total Books', stats['total']])
                    writer.writerow(['Read', stats['read']])
                    writer.writerow(['Currently Reading', stats['reading']])
                    writer.writerow(['Unread', stats['unread']])
                    writer.writerow(['Completion Rate (%)', f"{stats['completion_rate']:.2f}"])
                    writer.writerow(['Report Generated', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
                
                print(f"  Reading report saved as '{filename}'")
                print(f"  Location: {os.path.abspath(filename)}")
                return filename
                
            except Exception as e:
                print(f"Error generating CSV report: {e}")
                return None
                
        elif format.lower() == 'excel':
            try:
                import pandas as pd
                
                # Prepare data
                data = {
                    'Statistic': ['Total Books', 'Read', 'Currently Reading', 'Unread', 'Completion Rate (%)', 'Report Generated'],
                    'Value': [
                        stats['total'],
                        stats['read'],
                        stats['reading'],
                        stats['unread'],
                        f"{stats['completion_rate']:.2f}%",
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    ]
                }
                
                df = pd.DataFrame(data)
                filename = f"reading_report_{timestamp}.xlsx"
                df.to_excel(filename, index=False)
                
                print(f"  Excel report saved as '{filename}'")
                print(f"  Location: {os.path.abspath(filename)}")
                return filename
                
            except ImportError:
                print("  Pandas library not installed. Excel export requires 'pandas' package.")
                print("  Install it with: pip install pandas openpyxl")
                print("  Falling back to CSV format...")
                return self.generate_reading_report('csv')
            except Exception as e:
                print(f" Error generating Excel report: {e}")
                return None
        else:
            print(f" Unsupported format: {format}. Use 'csv' or 'excel'.")
            return None
# **Personal Book Collection Manager**
A command-line application to manage your personal library. Track books you've read, want to read, and generate comprehensive reading reports.

## **Features:**
- **Book Management**: add, view, search, and update books in your collection
- **Multiple Tables**: authors, genres, and books with proper relationships
- **Reading Tracking**: mark books as read, currently reading, or unread
- **Advanced Search**: filter by author, genre, publication year, or reading status
- **Statistics Dashboard**: view reading progress and collection insights
- **Report Generation**: export data to CSV or Excel format
- **Database Operations**: full CRUD functionality (Create, Read, Update operations)

## **Requirements:**
- Python 3.8 or higher
- pip (Python package installer)

## **Installation & Setup**
### **1. Clone the Repository:**
```bash
git clone https://github.com/shahd03/book-manager.git
cd book-manager
```

### **2. Create Virtual Environment:**
```bash
python -m venv venv
```

### **3. Install Dependencies:**
```bash
pip install -r requirements.txt
```
### **4. Initialize the Database:**
```bash
python main.py --init
```
### **5. Start the Application:**
```bash
python main.py
```

### **Available Commands:**
Once running, you can choose from these options:

1. **Add a new book**: enter book details including title, author, genre
2. **View all books**: display all books in your collection
3. **Search books**: filter by author, genre, or reading status
4. **Update book status**: mark as read/reading/unread
5. **View statistics**: see reading progress and collection insights
6. **Generate collection report**: export all books to CSV/Excel
7. **Generate reading report**: export reading statistics by genre
8. **Exit**: close the application

## **License**
This project is for educational purposes as part of the VIVES University of Applied Sciences assignment.

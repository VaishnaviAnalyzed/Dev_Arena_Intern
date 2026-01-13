import json
import os
from datetime import datetime, date, timedelta

# --- BOOK CLASS (Your logic with minor fixes for the UI) ---
class Book:
    def __init__(self, title, author, isbn, year=None):
        self.title = title
        self.author = author
        self.isbn = str(isbn)
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def to_dict(self):
        return {
            'title': self.title, 'author': self.author, 'isbn': self.isbn,
            'year': self.year, 'available': self.available,
            'borrowed_by': self.borrowed_by, 'due_date': str(self.due_date) if self.due_date else None
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data['title'], data['author'], data['isbn'], data.get('year'))
        book.available = data['available']
        book.borrowed_by = data.get('borrowed_by')
        if data.get('due_date'):
            book.due_date = data['due_date']
        return book

# --- LIBRARY MANAGER ---
class Library:
    def __init__(self):
        self.books = []
        # Sample data to make it work immediately
        self.seed_data()

    def seed_data(self):
        """Pre-loads the books you mentioned in your example"""
        sample_books = [
            {"title": "Python Crash Course", "author": "Eric Matthes", "isbn": "9781593279288", "year": 2019, "available": True},
            {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "isbn": "9781593275990", "year": 2015, "available": False, "borrowed_by": "MEM001", "due_date": "2024-02-15"},
            {"title": "Fluent Python", "author": "Luciano Ramalho", "isbn": "9781491946008", "year": 2022, "available": True}
        ]
        for b in sample_books:
            self.books.append(Book.from_dict(b))

    def search_books(self):
        print("\nSearch books by:")
        print("1. Title\n2. Author\n3. ISBN\n4. Show all available books")
        
        choice = input("\nEnter search option: ")
        query = ""
        results = []

        if choice == '1':
            query = input("Enter title to search: ").lower()
            results = [b for b in self.books if query in b.title.lower()]
        
        print(f"\nSearch Results for '{query}':")
        print("-" * 40)
        
        if not results:
            print("No books found.")
        else:
            for i, book in enumerate(results, 1):
                status = "Available" if book.available else f"Borrowed by {book.borrowed_by} (Due: {book.due_date})"
                print(f"{i}. {book.title}")
                print(f"   Author: {book.author}")
                print(f"   ISBN: {book.isbn}")
                print(f"   Year: {book.year}")
                print(f"   Status: {status}\n")
            print(f"Found {len(results)} books matching '{query}'")

# --- MAIN MENU LOOP ---
def main():
    lib = Library()
    
    while True:
        print("\n================================")
        print("    LIBRARY MANAGEMENT SYSTEM")
        print("================================")
        print(f"Loaded {len(lib.books)} books from file")
        print("Loaded 10 members from file") # Static for this example
        print("\n1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View All Books")
        print("7. View All Members")
        print("8. View Overdue Books")
        print("9. Save & Exit")
        print("0. Exit Without Saving")

        choice = input("\nEnter your choice: ")

        if choice == '5':
            lib.search_books()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("This feature is not implemented in this demo. Try Choice 5 or 0.")

if __name__ == "__main__":
    main()
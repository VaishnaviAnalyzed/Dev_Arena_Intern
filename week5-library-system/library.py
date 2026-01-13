from .book import Book
from .member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, choice, query):
        results = []
        if choice == '1': # Title
            results = [b for b in self.books if query.lower() in b.title.lower()]
        elif choice == '2': # Author
            results = [b for b in self.books if query.lower() in b.author.lower()]
        elif choice == '3': # ISBN
            results = [b for b in self.books if query in b.isbn]
        return results
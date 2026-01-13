# Library Management System 
## Project Description 
A comprehensive library management system built using Object-Oriented Programming principles. This system allows librarians to manage books, members, and borrowing operations efficiently. 

## What I Learned 
1. **OOP Principles**: Classes, objects, inheritance, and encapsulation
2. **Class Design**: How to design classes for real-world systems
3. **Class Relationships**: Understanding how different classes interact
4. **Method Implementation**: Creating methods that model real behaviors
5. **Data Persistence**: Saving and loading object data to files


## Features 
- ✅ Add, remove, and search for books
- ✅ Register and manage library members
- ✅ Borrow and return books with due dates
- ✅ Track overdue books and calculate fines
- ✅ Search books by title, author, or ISBN
- ✅ Limit maximum books per member
- ✅ Save/Load data to JSON files
- ✅ User-friendly menu interface
- ✅ Comprehensive error handling
  

## How to Run 
```
bash
cd week5-library-system
python -m library_system.main
 ```

## Class Structure 
```
python 
# Book Class
class Book:
def __init__(self, title, author, isbn):
self.title = title
self.author = author
self.isbn = isbn
self.available = True
self.borrowed_by = None
self.due_date = None

# Member Class
class Member:
def __init__(self, name, member_id):
self.name = name
self.member_id = member_id
self.borrowed_books = []
self.max_books = 5

# Library Class
class Library:
def __init__(self):
self.books = {}
self.members = {}
```

## Sample Menu 
``` 
================================
LIBRARY MANAGEMENT SYSTEM
================================
1. Add New Book
2. Register New Member
3. Borrow Book
4. Return Book
5. Search Books
6. View All Books
7. View All Members
8. View Overdue Books
9. Save & Exit
0. Exit Without

Saving Enter your choice:
```

## Sample Output 
``` 
Search Results for 'python':
----------------------------------------
1. Python Crash Course (ISBN: 9781593279288)
Author: Eric Matthes
Status: Available

2. Automate the Boring Stuff with Python (ISBN: 9781593275990)
Author: Al Sweigart
Status: Borrowed by John Doe (Due: 2024-02-15)

Library Statistics:
- Total Books: 125
- Available Books: 89
- Total Members: 45
- Books Borrowed: 36
- Overdue Books: 3
```

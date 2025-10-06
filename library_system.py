class Book:
    def __init__(self, title, author,available=True):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Added '{title}' by {author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed '{title}'")
                return
        print(f"'{title}' is not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You returned '{title}'")
                return
        print(f"'{title}' was not borrowed from this library")

    def show_available_books(self):
        available = [book.title for book in self.books if book.available]
        if available:
            print("Available books:", ", ".join(available))
        else:
            print("No books available")

    
# Create library instance
library = Library()
library.add_book("Python Basics", "Guido van Rossum")
library.add_book("Learning JavaScript", "Brendan Eich")
library.add_book("Atomic Habits", "James Clear")
library.add_book("Database Designs", "Connolly and Begg")

library.show_available_books()
library.borrow_book("Python Basics")
library.show_available_books()
library.return_book("Python Basics")
library.show_available_books()



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._book = []
        self._currentBooks = []
    def add_book(self, obj):
        self._book.append(obj)
    def check_out_book(self, title):
        for book in self._book:
            if book.title == title:
                book._is_checked_out = True
    def list_available_books(self):
        for book in self._book:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
    def return_book(self, title):
        for book in self._book:
            if book.title == title:
                book._is_checked_out = False
    

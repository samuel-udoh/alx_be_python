class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def return_book(self):
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True
    def is_available(self):
        return not self._is_checked_out
class Library:
    def __init__(self):
        self._book = []
    def add_book(self, obj):
        self._book.append(obj)
    def check_out_book(self, title):
        for book in self._book:
            if book.title == title:
                book.check_out()
    def list_available_books(self):
        for book in self._book:
            if book.is_available():
                print(f"{book.title} by {book.author}")
    def return_book(self, title):
        for book in self._book:
            if book.title == title:
                book.return_book()
    

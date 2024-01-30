class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
         for i in self.books:
             if i.author == book.author and i.title == book.title:
                 self.books.remove(i)

    def search_books(self, search_string):
        match_books = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                match_books.append(book)
        return match_books
                
                
            

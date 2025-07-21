class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f'{self.title}: {self.author}, {self.year}'


class Library:
    books: list()

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def find_book(self, title: Book):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(book.display_info())


# Приклад використання
library = Library()

book1 = Book(title="1984", author="George Orwell", year=1949)
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960)

library.add_book(book1)
library.add_book(book2)

print("📚 Список книг у бібліотеці:")
library.display_books()

found_book = library.find_book("1984")
if found_book:
    print("🔍 Знайдено книгу:", found_book.display_info())

library.remove_book("1984")

print("\n📚 Список книг після видалення:")
library.display_books()

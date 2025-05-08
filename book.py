# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

# Create an instance method display_book_count() to show the total number of books.

# Create a class method to create a book instance and increment the count.
# Create a class method to create a book instance and increment the count.

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
        self.display_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def display_book_count(self):
        print(f"Total books: {Book.total_books}")

    @classmethod
    def create_book(cls, title, author):
        return cls(title, author)
        
# Example usage:
book1 = Book.create_book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book.create_book("To Kill a Mockingbird", "Harper Lee")
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")
print(f"Total books created: {Book.total_books}")


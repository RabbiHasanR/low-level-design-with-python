# Real-Life Example: A Library System
# Consider a library system where a Library contains multiple Book objects. 
# The Book can exist independently of the Library, meaning a Book can be part of multiple libraries or exist without being part of any library at all.


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        return f"'{self.title}' by '{self.author}'"


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []
        
    
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)
    
    def list_books(self):
        return [str(book) for book in self.books]
    
    def __str__(self) -> str:
        return f"Library '{self.name}' with {len(self.books)} books"
    
    
    


# Create some book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Create a library object
library = Library("City Library")

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# List books in the library
print(library.list_books())  # Output: ["'1984' by George Orwell", "'To Kill a Mockingbird' by Harper Lee"]

# Remove a book and list again
library.remove_book(book1)
print(library.list_books())  # Output: ["'To Kill a Mockingbird' by Harper Lee"]

# The book still exists even if it's not part of the library
print(book1)  # Output: '1984' by George Orwell


# Aggregation in Built-In Python Classes
# While Python's built-in classes don’t explicitly use aggregation as a named pattern, the concept can be seen in many places 
# where objects are used together in a loosely coupled manner. 
# For example, the relationship between a list (or any collection) and 
# its elements can be seen as aggregation. The list "has-a" collection of items, but the items can exist independently of the list.


# A list of objects
books = [Book("1984", "George Orwell"), Book("The Great Gatsby", "F. Scott Fitzgerald")]

# The books exist independently of the list
print(books[0])  # Output: '1984' by George Orwell

# Remove a book from the list, but the book still exists
removed_book = books.pop(0)
print(removed_book)  # Output: '1984' by George Orwell

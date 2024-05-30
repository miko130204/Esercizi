#Exercise 1: 

import math
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


#Exercise 2:

class MathOperations:
    def __init__(self, n1: int, n2: int):
        self.n1: int = n1
        self.n2: int = n2

    def add(self):
        result = self.n1 + self.n2
        return result
    
    def multiply(self):
        result = self.n1 * self.n2
        return result


#Exercise 3: 

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
    
    def from_string(cls, book_str: str):
        title, author, isbn = book_str.split(', ')
        return cls(title, author, isbn)

class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)
    
    def return_book(self, book: Book):
        self.borrowed_books.remove(book)
    
    def __str__(self):
        borrowed_books_str = ', '.join([str(book) for book in self.borrowed_books])
        return f"Member(name='{self.name}', member_id='{self.member_id}', borrowed_books=[{borrowed_books_str}])"
    
    def from_string(cls, member_str: str):
        name, member_id = member_str.split(', ')
        return cls(name, member_id)

class Library:
    total_books = 0
    
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book: Book):
        self.books.append(book)
        Library.total_books += 1
    
    def remove_book(self, book: Book):
        self.books.remove(book)
        Library.total_books -= 1
    
    def register_member(self, member: Member):
        self.members.append(member)
    
    def lend_book(self, book: Book, member: Member):
        if book in self.books and member in self.members:
            member.borrow_book(book)
            self.remove_book(book)
    
    def __str__(self):
        books_str = ', '.join([str(book) for book in self.books])
        members_str = ', '.join([str(member) for member in self.members])
        return f"Library(total_books={Library.total_books}, books=[{books_str}], members=[{members_str}])"
    
    def library_statistics(cls):
        return f"Total number of books: {cls.total_books}"


#Exercise 4


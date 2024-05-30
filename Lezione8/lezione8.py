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
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
    
    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
    
    def from_string(cls, book_str: str):
        title, author, isbn = book_str.split(', ')
        return cls(title, author, isbn)
    

#Exercise 4


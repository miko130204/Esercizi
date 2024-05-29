class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            return "Book is already borrowed"

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            return "Book was not borrowed"
        

class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, book: Book):
        if book.book_id not in self.books:
            self.books[book.book_id] = Book(book.book_id, book.title, book.author)
            return "Book has been added"
        else:
            return "Book with this ID already exists"

    def borrow_book(self, book_id: str):
        if book_id not in self.books:
            return "Book not found"
        else:
            book = self.books[book_id]
            book.borrow_book()
            return "The book has been borrowed"

    def return_book(self, book_id: str):
        if book_id not in self.books:
            return "Book not found"
        else:
            book = self.books[book_id]
            book.return_book()
            return "The book has been returned"

    def get_not_borrowed_books(self):
        not_borrowed_books = [book.title for book in self.books.values() if not book.is_borrowed]
        return not_borrowed_books
    
library1 = Library()
book1: Book = Book("1", "Berserk", "Author")
#print(library1.add_book(book1))
#print(library1.borrow_book(book1.book_id))
#print(library1.return_book(book1.book_id))
#print(library1.get_not_borrowed_books())



# 2

class Movie:
    def __init__(self, title: str, director: str):
        self.name: str = title
        self.director: str = director

class Movie_catalog:
    def __init__(self):
        self.movies: dict[str, list[Movie]] = {}

    def add_movie(self, movie: Movie):
        if movie.director not in self.movies:
            self.movies[movie.director] = []
        self.movies[movie.director].append(Movie(movie.name, movie.director))
        return "Movie has been added"
    
    def remove_movie(self, title: str):
        for director, movies in self.movies.items():
            for movie in movies:
                if movie.name == title:
                    movies.remove(movie)
                    if not movies:
                        del self.movies[director]
                    return "Movie has been removed"
        return "Movie not found"
    
    def list_directors(self):
        return list(self.movies.keys())
        
    def get_movies_by_director(self, director: str):
        if director in self.movies:
            return [movie.name for movie in self.movies[director]]
        return "Director not found"
    
    def search_movies_by_title(self, title: str):
        result = {}
        for director, movies in self.movies.items():
            matching_movies = [movie.name for movie in movies if title.lower() in movie.name.lower()]
            if matching_movies:
                result[director] = matching_movies
        if result:
            return result
        return "No movies found with the given title"


catalog = Movie_catalog()
catalog.add_movie(Movie("Inception", "Christopher Nolan"))
catalog.add_movie(Movie("Interstellar", "Christopher Nolan"))
catalog.add_movie(Movie("Pulp Fiction", "Quentin Tarantino"))

print(catalog.list_directors())
print(catalog.get_movies_by_director("Christopher Nolan"))
print(catalog.search_movies_by_title("inception"))
print(catalog.remove_movie("Inception"))
print(catalog.get_movies_by_director("Christopher Nolan"))

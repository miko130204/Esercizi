class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise ValueError("Book was not borrowed")


class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise ValueError("Book not borrowed by this member")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
        else:
            raise ValueError("Book with this ID already exists")

    def register_member(self, member_id: str, name: str):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
        else:
            raise ValueError("Member with this ID already exists")

    def borrow_book(self, member_id: str, book_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[book_id]
        member.borrow_book(book)

    def return_book(self, member_id: str, book_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[book_id]
        member.return_book(book)

    def get_borrowed_books(self, member_id: str):
        if member_id in self.members:
            member = self.members[member_id]
            return [book.title for book in member.borrowed_books]
        else:
            raise ValueError("Member not found")


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

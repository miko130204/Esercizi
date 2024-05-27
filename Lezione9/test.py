# 6

class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool = False):
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = is_borrowed

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
        else:
            raise ValueError("Book was not borrowed")

class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):
        if book not in self.borrowed_books and book.is_borrowed == False:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            raise ValueError("Book not borrowed by this member")

class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

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
        if member_id not in self.members:
            raise ValueError("Member ID does not exist")
        
        member = self.members[member_id]
        return [book.title for book in member.borrowed_books]
    

# 8

class Account:
    def __init__(self, account_id: str):
        self.account_id: str = account_id
        self.balance: float = 0.0

    def deposit(self, amount: int):
        self.balance += amount
    
    def get_balance(self):
        return self.balance
    

class Bank:
    def __init__(self):
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id: str) -> Account:
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")
        else: 
            account = Account(account_id)
            self.accounts[account_id] = account
            return account

    def deposit(self, account_id: str, amount: float):
        self.accounts[account_id].deposit(amount)
        
    def get_balance(self, account_id: str):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        else:
            return self.accounts[account_id].get_balance()







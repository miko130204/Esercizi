# 1

def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for word in word_set:
            if dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
                break
    return dp[-1]


# 2

def valid_sudoku(board: list[list[str]]) -> bool:
    def is_valid_unit(unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
    
    def is_valid_row(board):
        for row in board:
            if not is_valid_unit(row):
                return False
        return True
        
    def is_valid_col(board):
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        return True
            
    def is_valid_square(board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j+3)]
                if not is_valid_unit(square):
                    return False
        return True
    
    return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)
        

# 3


# 4

def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if sorted_s == sorted_t:
        return True
    else:
        return False


# 5

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


# 6

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    def is_mirror(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.val == node2.val) and is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)

    def build_tree(index):
        if index >= len(tree):
            return None
        node = TreeNode(tree[index])
        node.left = build_tree(2 * index + 1)
        node.right = build_tree(2 * index + 2)
        return node

    if not tree:
        return True
    root = build_tree(0)
    return is_mirror(root.left, root.right)


# 7

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







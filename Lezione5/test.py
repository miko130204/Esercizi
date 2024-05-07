# 2. Book Collection:

# Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
# This function should return a dictionary where the author's name is the key and the value is a list of their books. 
# Demonstrate this function by adding books for different authors.

# Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
# This function should return an updated dictionary.


def add_book(name, books):
    book_list = {'author': name, 'books': books}
    return book_list

def delete_book(name, books):
    book_list = {'author': name, 'books': books}
    book_list['books'].remove(books)
    return book_list

author = "Edgar Allan Poe"
books = ["Black Cat", "sss"]

print(add_book(author, books))
print(delete_book(author, books))
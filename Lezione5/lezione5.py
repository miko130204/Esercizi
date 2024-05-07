# 1. Create a Playlist:
# Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
# The function should return a dictionary with the playlist name and a set of songs. Call the function with 
# different numbers of songs to demonstrate flexibility.
# Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating 
# whether it is liked (True or False). This function should return an updated dictionary.

playlist = {}

def create_playlist(playlist_name, songs):
    playlist = (playlist_name, songs)
    return playlist

def add_like(songs, playlist_name, liked):
    playlist = (playlist_name, songs, liked)
    if liked == True:
        return playlist
    else:
        return playlist

songs = {"GRINDHOUSE", "RESPIRA"}
playlist_name = "Road Trip"
print(create_playlist(playlist_name, songs))

answer = input(f"Do you like {playlist_name}? ")
if answer == "yes":
    print(add_like(songs, playlist_name, liked = True))

else:
    print(add_like(songs, playlist_name, liked = False))


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
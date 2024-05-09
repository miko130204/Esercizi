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
    if liked == True:
        playlist = (playlist_name, songs, liked)
        return playlist
    else:
        playlist = (playlist_name, songs)
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
    
    for book in list(books):
        book_list['books'].remove(book)
    return book_list

author = "Edgar Allan Poe"
books = ["Black Cat", "sss"]

print(add_book(author, books))
print(delete_book(author, books))


# 3. Personal Info:
# Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
# Make occupation, location, and age optional parameters. Use this function to create profiles for different people, 
# demonstrating how it handles these optional parameters.

def build_profile(name, surname, occupation = None, location = None, age = None):
    profile = {'name': name, 'surname': surname}
    if occupation:
        profile['occupation'] = occupation
    if location:
        profile['location'] = location
    if age:
        profile['age'] = age
    return profile
     

print(build_profile(name = "Mario", surname = "Rossi", occupation = "Worker", age = "27"))
print(build_profile(name = "Mario", surname = "Rossi"))
print(build_profile(name = "Mario", surname = "Rossi", age = "27"))


# 4. Event Organizer:
# Write a function called plan_event() that accepts an event name, a list of participants, and an hour. The function should 
# return a dictionary that includes the event name and a list of the participants. Call this function with varying numbers 
# of participants to plan different events.
# Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

def plan_event(name, participants, time):
    event = {'name': name, 'participants': participants, 'time': time}
    return event

def modify_event(dictionary, name, participants, time):
    event = {'dictionary': dictionary, 'name': name, 'participants': participants, 'time': time}
    return event


name = "Code Workshop"
print(plan_event(name, ["Alice", "Bob", "Charlie"],"4pm"))

dictionary = {}
print(modify_event(dictionary, name, ["Alice", "Bob"], "6pm"))


# 5. Shopping List:
# Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. It should 
# return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.
# Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item 
# from that store's shopping list.

class Shopping:
    def __init__(self, name: str, items: list):
        self._name: str = name
        self._items: list = items
        self._shopping_list = {'name': name, 'items': items}
    
    def get_list(self):
        print(self._shopping_list['items'])

store = "Grocery Store"
shopping_list = {"Milk", "Eggs", "Bread"}

shopping_list1: Shopping = Shopping(store, shopping_list)

shopping_list1.get_list()
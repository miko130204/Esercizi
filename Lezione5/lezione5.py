# Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
# The function should return a dictionary with the playlist name and a set of songs. Call the function with 
# different numbers of songs to demonstrate flexibility.
# Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating 
# whether it is liked (True or False). This function should return an updated dictionary.


def create_playlist(param1, dictionary):
    return param1, dictionary

def add_like(dictionary, name, liked):
        return dictionary, name, liked

songs = {"Song 1", "Song 2"}

print(create_playlist("Road Trip", songs))

print(add_like(songs, "Road Trip", liked=True))
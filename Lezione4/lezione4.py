# 8-1. Write a function called display_message() that prints one sentence telling everyone what you are learning 
# about in this chapter. Call the function, and make sure the message displays correctly.

def display_message(param1):
    message = f"In this chapter we are learning about {param1}"
    return message
#learn = input("What are you learning in this chapter? ")
#print(display_message(learn))


# 8-2. Write a function called favorite_book() that accepts one parameter, title. The function should print a message, 
# such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as 
# an argument in the function call.

def favorite_book(title):
    message = f"One of my favorite books is {title}"
    return message

#answer = input("What is your favorite book? ")
#print(favorite_book(answer))


# 8-3. Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once 
# using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(param1,param2):
    message = f"The size of the tshirt is {param1} and the text printed on the tshirt is \"{param2}\""
    return message

#size = input("What is you tshirt size? ")
#text = input("What text do you want to print on the tshirt? ")

#print(make_shirt(size,text))


# 8-4. Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(param1,param2):
    message = f"The size of the tshirt is {param1} and the text printed on the tshirt is \"{param2}\""
    return message

print("The default size id large and the default text is \"I love Python\"")
answer = input("If you want the default shirt type \"default\"\nIf you want to change the size type \"size\"\n if you want to change text type \"text\"\nand if you want to change both type\"both\" ")

if (answer == "default"):
    param1 = "large"
    param2 = "I love Python"
    print(make_shirt(param1=param1, param2=param2))
elif (answer == "size"):
    param2 = "I love Python"
    size = input("What is you tshirt size? ")
    print(make_shirt(size, param2=param2))
elif (answer == "text"):
    param1 = "large"
    text = input("What text do you want to print on the tshirt? ")
    print(make_shirt(param1=param1, param2 = text))
elif (answer == "both"):
    size = input("What is you tshirt size? ")
    text = input("What text do you want to print on the tshirt? ")
    print(make_shirt(size,text))


# 8-5. Write a function called describe_city() that accepts the name of a city and its country. The function should print 
# a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function 
# for three different cities, at least one of which is not in the default country.

def describe_city(param1, param2):
    message = f"{param1} is in {param2}"
    return message

country = "Italy"
print(describe_city(param1= "Venice", param2 = country))
print(describe_city(param1= "Turin", param2 = country))
print(describe_city(param1= "Berlin", param2 = "Germany"))


# 8-6. Write a function called city_country() that takes in the name of a city and its country. The function should return 
# a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print 
# the values that are returned.

def city_country(param1, param2):
    message = f"{param1}, {param2}"
    return message

city1 = "Rome"
country1 = "Italy"
city2 = "Paris"
country2 = "France"
city3 = "Berlin"
country3 = "Germany"

print(city_country(city1, country1))
print(city_country(city2, country2))
print(city_country(city3, country3))


# 8-7. Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist
# name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three
# dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information 
# correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling 
# line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes 
# the number of songs on an album.

def make_album(param1, param2, param3 = None):
    album = {'artist': param1, 'title': param2}
    if param3:
        album ['songs'] = param3
    return album

album1 = make_album('Eminem', 'Encore')
album2 = make_album('Metallica', 'Kill \'em all', 12)
album3 = make_album('AC/DC', 'Thunderstruck', 10)

print(album1)
print(album2)
print(album3)


# 8-8. Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you
 # have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit 
 # value in the while loop.

def make_album(param1, param2, param3 = None):
    album = {'artist': param1, 'title': param2}
    if param3:
        album ['songs'] = param3
    return album

answer = ""
while(answer != "stop"):
    artist_input = input("Type in your artist ")
    album_input = input("Which album? ")
    songs_input = input("How many songs ")
    album = make_album(param1 = artist_input, param2 = album_input, param3 = songs_input)
    answer = input("If you're done type \"stop\", else just press enter ")
    print(album)


# 8-9. Make a list containing a series of short text messages. Pass the list to a function called show_messages(), 
# which prints each text message.

def show_messages(param1):
    mess_list = []
    mess_list.append(param1)
    for message in mess_list:
        return message

answer = ""
while(answer != "stop"):
    answer = input("Type a short message (If you're done type \"stop\") ")
    messages = show_messages(answer)
    print(messages)


# 8-10. Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text 
# message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both 
# of your lists to make sure the messages were moved correctly.

def show_messages(param1):
    mess_list = []
    mess_sent  = []
    mess_list.append(param1)
    for message in mess_list:
        return message
    for message in mess_sent:
        return message

answer = ""
while(answer != "stop"):
    answer = input("Type a short message (If you're done type \"stop\") ")
    messages = show_messages(answer)
    print(messages)


# BUBBLE SORT

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if (A[j] > A[j+1]):
                var = A[j]
                A[j] = A[j+1]
                A[j+1] = var
    return A

bubble_list = [2,5,1,2,6,3,8,4,7]
print(bubble_sort(bubble_list))
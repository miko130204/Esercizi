# Mikolaj
# 17/04/24
print ("Salve!")


# 2-3 Use a variable to represent a person’s name, and print a message to 
# that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”

person = "Eric"
print(f"Hello {person}, would you like to learn some Python today?")


# 2-4 Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.

print(f"Hello {person.lower()}")
print(f"Hello {person.upper()}")
print(f"Hello {person.title()}")


# 2-5. Famous Quote: Find a quote from a famous person you admire. 
# Print the quote and the name of its author. Your output should look 
# something like the following, including the quotation marks: Albert 
# Einstein once said, “A person who never made a mistake never tried anything new.”

famous_name = "Optimus Prime"
quote = "At the end of this day, one shall stand, one shall fall!"
print(f"{famous_name} once said, \"{quote}\".")


#2-6. Repeat Exercise 2-5, but this time, represent the famous person’s
# name using a variable called famous_person. Then compose your message 
# and represent it with a new variable called message. Print your message. 

famous_person = "Optimus Prime"
quote = "At the end of this day, one shall stand, one shall fall!"
message = f"{famous_person} once said, \"{quote}\"." 
print(f"{message}")


# 2-8. Python has a removesuffix() method that works exactly like removeprefix(). 
# Assign the value 'python_notes.txt' to a variable called filename. Then use the 
# removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = "python_notes.txt"
print(f"{filename.removesuffix('.txt')}")


# 3-1. Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

friends = ["Alfonso", "Riccardo", "Edwin"]
print(friends[0])
print(friends[1])
print(friends[2])


# 3-2. Start with the list you used in Exercise 3-1, but instead of just printing
#  each person’s name, print a message to them. The text of each message should be 
# the same, but each message should be personalized with the person’s name.

print(f"Hi {friends[0]} how are you?")
print(f"Hi {friends[1]} how are you?")
print(f"Hi {friends[2]} how are you?")


# 3-3. Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples. Use your list to print a series of 
# statements about these items, such as “I would like to own a Honda motorcycle.”

transport = ["Car", "Motorcycle"]
print(f"I would like to have a Yamaha {transport[1]} and a BMW {transport[0]}")


# 3-4. If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. Then 
# use your list to print a message to each person, inviting them to dinner.

guest_list = ["Dante", "Kratos", "Cicciogamer89"]
print(f"Hi {guest_list[0]}, I would like to invite you to dinner tonight")
print(f"Hi {guest_list[1]}, I would like to invite you to dinner tonight")
print(f"Hi {guest_list[2]}, I would like to invite you to dinner tonight")


# 3-5. You just heard that one of your guests can’t make the dinner, so you need to send 
# out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

guest_list = ["Dante", "Kratos", "Cicciogamer89"]
print(f"Unfortunately {guest_list[2]} can't make it to dinner.")
guest_list.remove("Cicciogamer89")
guest_list.append("Rick")
print(f"Hi {guest_list[0]}, I would like to invite you to dinner tonight.")
print(f"Hi {guest_list[1]}, I would like to invite you to dinner tonight.")
print(f"Hi {guest_list[2]}, I would like to invite you to dinner tonight.")


# 3-6. You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

guest_list = ["Dante", "Kratos", "Rick", "Jordi"]
print(f"Hello everyone, I just found a bigger table so there will be 3 more people :) ")
guest_list.insert(0,"Gianni")
guest_list.insert(3, "Stan Lee")
guest_list.append("Johnny")
i=0
while i<6:
    print(f"Hi {guest_list[i]}, I would like to invite you to dinner tonight.")
    i += 1


# 3-7. You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ["Gianni", "Johnny", "Kratos", "Stan Lee", "Jordi", "Rick", "Dante"]
print(f"Hello everyone, I'm really sorry but the only avaivable table is for only 2 person :( ")
i = 0
while i !=4:
    print(f"I'm sorry {guest_list.pop(i)} but I can't invite you to dinner")
    i += 1
print(f"Hi {guest_list[0]}, you are still invited to dinner tonight.")
print(f"Hi {guest_list[1]}, you are still invited to dinner tonight.")


# 3-8. Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# • Use sort() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sort() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

places = ["Los Angeles ", "New York ", "Paris ", "Bucarest ", "Warsaw "]
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)


# 3-9. Working with one of the programs from Exercises 3, use len() 
# to print a message indicating the number of people you’re inviting to dinner.
# I took it from ex 3-5

guest_list = ["Dante", "Kratos", "Cicciogamer89"]
print(f"There will be {len(guest_list)} guest at dinner tonight.")


# 3-10. Think of things you could store in a list. For example, you could make a list 
# of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

cars = ["BMW", "Audi", "Mercedes", "Bugatti", "Ferrari"]
print(cars)
print(f"{cars[0].lower()}")
cars.insert(0,"Porsche")
print(cars)
cars.append("Lamborghini")
print(cars)
cars.remove("Audi")
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.sort()
cars.reverse()
print(cars)
cars.sort()
print(cars)


# 6-1. Use a dictionary to store information about a person you know. Store their first name, 
# last name, age, and the city in which they live. You should have keys such as first_name, 
# last_name, age, and city. Print each piece of information stored in your dictionary.

persons = {"first_name": "Enzo", "last_name": "Ferrari", "age": 30, "city": "Maranello"}, {"first_name": "Ferruccio", "last_name": "Lamborghini", "age": 35, "city": "Bologna"}, {"first_name": "Tony", "last_name": "Effe", "age": 40, "city": "Roma"}
for person in persons:
    print(f" Name: {person['first_name']}\n Last Name: {person['last_name']}\n Age: {person['age']}\n City: {person['city']}\n//////////")


# 6-2. Use a dictionary to store people’s favorite numbers. Think of five names, 
# and use them as keys in your dictionary. Think of a favorite number for each person, and store each 
# as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, 
# poll a few friends and get some actual data for your program.

persons = {"name": "Dante", "fav_number": 3}, {"name": "Jerry", "fav_number": 10}, {"name": "Rick", "fav_number": 11}, {"name": "Edwin", "fav_number": 5}, {"name": "Mia", "fav_number": 17}
for person in persons:
    print(f"{person['name']}'s favorite number is {person['fav_number']}\n//////////")


# 6-3. A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word 
# followed by a colon and then its meaning, or print the word on one line and then print 
# its meaning indented on a second line. Use the newline character (\n) to insert a blank 
# line between each word-meaning pair in your output.

glossary = {"name": "for", "meaning": "loop that iterates through code in its body for a set amount of times until a condition is met"}, {"name": "while", "meaning": "controls flow statement which repeatedly executes a block of code until the condition is satisfied"}, {"name": "remove", "meaning": "remove an item from a list by its value and not by its index number"}, {"name": "print", "meaning": "print the specified message to the screen"}, {"name": "append", "meaning": "used to add a single item to certain collection types"}
for words in glossary:
    print(f"Definition of {words['name']}: {words['meaning']}\n//////////")


# 6-7. Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing 
# different people, and store all three dictionaries in a list called people. Loop through your 
# list of people. As you loop through the list, print everything you know about each person.

persons = {"first_name": "Enzo", "last_name": "Ferrari", "age": 30, "city": "Maranello"},{"first_name": "Ferruccio", "last_name": "Lamborghini", "age": 35, "city": "Bologna"},{"first_name":"Tony", "last_name": "Effe", "age": 40, "city": "Roma"},{"first_name":"Vladimir", "last_name": "Putin", "age": 61, "city": "Moscow"},{"first_name":"Gianni", "last_name": "Morandi", "age": 60, "city": "Monghidoro"}
for person in persons:
    print(f" Name: {person['first_name']}\n Last Name: {person['last_name']}\n Age: {person['age']}\n City: {person['city']}\n//////////")


# 6-8. Make several dictionaries, where each dictionary represents a different pet. In each 
# dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a 
# list called pets. Next, loop through your list and as you do, print everything you know about each pet. 

pets = {"animal": "dog", "owner": "Jack"}, {"animal": "cat", "owner": "Marco"}, {"animal": "bird", "owner": "Rick"}
for pet in pets:
    print(f"The animal is a {pet['animal']} and the owner is {pet['owner']}")


# 6-9. Make a dictionary called favorite_places. Think of three names to use 
# as keys in the dictionary, and store one to three favorite places for each person. To make 
# this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {"name": "Jack", "fav_place": "Rome"},{"name": "Marco", "fav_place": "Paris"},{"name": "Rick", "fav_place": "Berlin"}
for place in favorite_places:
    print(f"{place['name']}'s favorite place is {place['fav_place']}")


# 6-10. Modify your program from Exercise 6-2 so each person can have more than 
# one favorite number. Then print each person’s name along with their favorite numbers.

persons = {"name": "Dante", "fav_number": [3, 33, 333]}, {"name": "Jerry", "fav_number": [2, 4]}, {"name": "Rick", "fav_number": [11, 6]}, {"name": "Edwin", "fav_number": [5, 10]}, {"name": "Mia", "fav_number": [3, 99]}
for person in persons:
    print(f"{person['name']}'s favorite number is {person['fav_number']}\n//////////")


# 6-11. Make a dictionary called cities. Use the names of three cities as keys in 
# your dictionary. Create a dictionary of information about each city and include the country 
# that the city is in, its approximate population, and one fact about that city. The keys for 
# each city’s dictionary should be something like country, population, and fact. Print the name 
# of each city and all of the information you have stored about it.

info_cities = {"name": "Milan", "country": "Italy", "population": 59000000, "fact": "Rome is over 2000 years old"}, {"name": "Paris", "country": "France", "population": 68000000, "fact": "The form of government in France is Republic"}, {"name": "Berlin", "country": "Germany", "population": 84000000, "fact": "Berlin has the largest train station in Europe"}
for city in info_cities:
    print(f"{city['name']} is a city in {city['country']}, the population is {city['population']} and a fact is: {city['fact']}\n//////////")
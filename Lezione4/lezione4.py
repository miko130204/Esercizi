# 8-1. Write a function called display_message() that prints one sentence telling everyone what you are learning 
# about in this chapter. Call the function, and make sure the message displays correctly.

def display_message(param1):
    print(f"In this chapter we are learning about {param1}")
    return 
#learn = input("What are you learning in this chapter? ")
#print(display_message(learn))


# 8-2. Write a function called favorite_book() that accepts one parameter, title. The function should print a message, 
# such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as 
# an argument in the function call.

def favorite_book(title):
    print(f"One of my favorite books is {title}")

#answer = input("What is your favorite book? ")
#print(favorite_book(answer))


# 8-3. Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once 
# using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(param1,param2):
    print(f"The size of the tshirt is {param1} and the text printed on the tshirt is \"{param2}\"")

#size = input("What is you tshirt size? ")
#text = input("What text do you want to print on the tshirt? ")

#print(make_shirt(size,text))


# 8-4. Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(param1,param2):
    print(f"The size of the tshirt is {param1} and the text printed on the tshirt is \"{param2}\"")

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
    print(f"{param1} is in {param2}")

country = "Italy"
print(describe_city(param1= "Venice", param2 = country))
print(describe_city(param1= "Turin", param2 = country))
print(describe_city(param1= "Berlin", param2 = "Germany"))

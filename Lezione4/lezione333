# 4-1. Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
# and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just 
# the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an 
# additional sentence, such as I really love pizza!

pizzas = ["Margherita", "Diavola", "Capricciosa"]

for pizza in pizzas:
    if (pizza == "Margherita"):
        print("I like margherita")

    elif (pizza == "Diavola"):
        print("I kinda like diavola")

    elif (pizza == "Capricciosa"):
        print("I don't like capricciosa")

print(f"I really love pizza. my favorite is {pizzas[0]}")


# 4-2. Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. You could print 
# a sentence, such as Any of these animals would make a great pet!

animals = ["Tiger", "Lynx", "Cat"]

for animal in animals:
    if (animal == "Tiger"):
        print("A tiger could be a pet even if its a wild animal")

    elif (animal == "Cat"):
        print("A cat can be a great pet")

    elif (animal == "Lynx"):
        print("A lynx could be a better pet instead of the tiger")

print("All those animals are feline and they would make a great pet.")


# 4-3. Use a for loop to print the numbers from 1 to 20, inclusive.

i = 0
while (i<20):
    i += 1
    print(i)


# 4-4. Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

i = 0
while (i<1000000):
    i += 1
    #print(i)


# 4-5. Make a list of the numbers from one to one million, and then use min() and max() 
# to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see 
# how quickly Python can add a million numbers.

i = 0
num_list = []
while (i<1000000):
    i += 1
    num_list.append(i)
print(min(num_list),max(num_list))
print(sum(num_list))


# 4-6. Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)


# 4-7. Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

multiples_3 = list(range(2, 31, 3))
for number in multiples_3:
    print(number)

# 4-8. A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 
# in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a 
# for loop to print out the value of each cube.

i=0
n=1
cube = []
while (i<10):
    cube.append(n**3)
    i += 1
    n += 1
print(cube)


# 4-9. Use a list comprehension to generate a list of the first 10 cubes.

cube = [n**3 for n in range (1, 11)]
print(cube)


# 4-10. Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

num_list = [1,2,3,4,5,6,7,8,9]
print(num_list[:3])
print(num_list[3:6])
print(num_list[-3:])


# 4-11. Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. 
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored 
# in the appropriate list.

friend_pizzas = ["Margherita", "Diavola", "Capricciosa"]
pizzas.append("4 Stagioni")
friend_pizzas.append("Napoli")

print(f"My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("////////")
print(f"My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)


# 4-12. All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version 
# of foods.py, and write two for loops to print each list of foods.

"alreay done in excercise 4-11"


# 4-15. Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

"I already used pep8"


# 5-1. Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.


number = 4
print("Is number == 4? I predict True")
print(number == 4)

fruit = "strawberry"
print("\nIs fruit != strawberry? I predict True")
print(fruit != "strawberry")

age = 17
print("\nIs age > 18? I predict False")
print(age > 18)

animals = ["cat", "dog", "bird"]
print("\nIs bird in animals? I predict Flase")
print('bird' in animals)


# 5-2. You don’t have to limit the number of tests you cre-
# ate to 10. If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

# string equal to
string = "hello"
if (string == "hello"):
    print(True)
else:
    print(False)

string = "hell"
if (string == "hello"):
    print(True)
else:
    print(False)

#lower method
string = "HELLO"
if (string.lower() == "hello"):
    print(True)
else:
    print(False)

string = "hello"
if (string.lower() == "HELLO"):
    print(True)
else:
    print(False)

#number equal to
num = 4
if (num == 4):
    print(True)
else:
    print(False)

num = 3
if (num == 4):
    print(True)
else:
    print(False)

#number greater than
num = 4
if (num > 3):
    print(True)
else:
    print(False)

num = 3
if (num > 4):
    print(True)
else:
    print(False)

#number greater or equal
num = 5
if (num >= 4 ):
    print(True)
else:
    print(False)

num = 4
if (num >= 5 ):
    print(True)
else:
    print(False)

#number lower or equal
num = 4
if (num <= 5 ):
    print(True)
else:
    print(False)

num = 5
if (num <= 4 ):
    print(True)
else:
    print(False)

#and keyword
num = 4
if (num <= 5 and num <= 6):
    print(True)
else:
    print(False)

num = 5
if (num <= 4 and num >= 6):
    print(True)
else:
    print(False)

#or keyword
num = 4
if (num <= 5 or num <= 6):
    print(True)
else:
    print(False)

num = 5
if (num <= 4 or num >= 6):
    print(True)
else:
    print(False)

#list
num_list = [1,2,3]
if (1 in num_list):
    print(True)
else:
    print(False)

num_list = [1,2,3]
if (4 in num_list):
    print(True)
else:
    print(False)

#not in list
num_list = [1,2,3]
if (4 not in num_list):
    print(True)
else:
    print(False)

num_list = [1,2,3]
if (3 not in num_list):
    print(True)
else:
    print(False)


# 5-3. Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

#true
alien_color = 'green'
if (alien_color == 'green'):
    print("You just earned 5 points")

#false
alien_color = 'red'
if (alien_color == 'green'):
    print("You just earned 5 points")


# 5-4. Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# • Write one version of this program that runs the if block and another that runs the else block.

#if block
alien_color = 'green'
if (alien_color == 'green'):
    print("You just earned 5 points for shooting the alien")
else:
    print("You just earned 10 points")

#else block
alien_color = 'yellow'
if (alien_color == 'green'):
    print("You just earned 5 points for shooting the alien")
else:
    print("You just earned 10 points")
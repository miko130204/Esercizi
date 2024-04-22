# 4-1. Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
# and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just 
# the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an 
# additional sentence, such as I really love pizza!

pizzas = ["Margherita", "Diavola", "Capricciosa"]
i = 0
while (i<3):
    print(pizzas[i])
    i += 1
i = 0
while (i<3):
    print(f"I like {pizzas[i]} pizza")
    i += 1
print(f"I really love pizza. my favorite is {pizzas[0]}")


# 4-2. Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. You could print 
# a sentence, such as Any of these animals would make a great pet!

animals = ["Tiger", "Lynx", "Cat"]
i = 0
while (i<3):
    print(animals[i])
    i += 1
i = 0
while (i<3):
    print(f"A {animals[i]} could be a great pet")
    i += 1
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
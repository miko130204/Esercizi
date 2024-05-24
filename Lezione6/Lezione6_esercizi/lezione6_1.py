# 9-1

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name: str = restaurant_name
        self.cuisine_type: str = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant():
        print("The restaurnat is open!")


restaurant1: Restaurant = Restaurant("Grande Egitto", "Italian")
#Restaurant.describe_restaurant(restaurant1)
#Restaurant.open_restaurant()


# 9-2

restaurant2: Restaurant = Restaurant("Sushiko", "Japanese")
restaurant3: Restaurant = Restaurant("Daje Roma", "Roman")

#restaurant1.describe_restaurant()
#restaurant2.describe_restaurant()
#restaurant3.describe_restaurant()


# 9-3

class User:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email

    def describe_user(self):
        print(f"Name: {self.first_name}")
        print(f"Surname: {self.last_name}")
        print(f"Email: {self.email}\n")
    
    def greet_user(self):
        print(f"Hello {self.first_name}, how are you?")
    

user1: User = User("Albert", "Einstein", "AlbertEin@gmail.com")
user2: User = User("Marc", "Marquez", "Marquez93@gmail.com")
user3: User = User("Valentino", "Rossi", "Rossi46@gmail.com")

#user1.describe_user()
#user1.greet_user()
print()
#user2.describe_user()
#user2.greet_user()
print()
#user3.describe_user()
#user3.greet_user()


# 9-4 

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name: str = restaurant_name
        self.cuisine_type: str = cuisine_type
        self.number_served: int = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, x: int):
        self.number_served = x

    def increment_number_served(self, y: int):
        self.number_served += y


restaurant = Restaurant("Sushiko", "Japanese")

restaurant.number_served = 5
#print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(10)
#print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(25)
#print(f"Number of customers served: {restaurant.number_served}")


# 9-5

class User:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.login_attempts: int = 0

    def describe_user(self):
        print(f"Name: {self.first_name}")
        print(f"Surname: {self.last_name}")
        print(f"Email: {self.email}\n")
    
    def greet_user(self):
        print(f"Hello {self.first_name}, how are you?")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)


#user1.increment_login_attempts()
#user1.increment_login_attempts()
#user1.reset_login_attempts()


# 9-6

#An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 
#9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice 
#cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, flavours: list):
        Restaurant.__init__(self, restaurant_name, cuisine_type)
        self.flavours: list = flavours

    def print_flavours(self):
        print(f"The flavours are: {self.flavours}")

flavours_list: list = ["Lemon", "Nutella", "Vanilla", "Strawberry", "Mango"]
stand1 = IceCreamStand("Ping Pong", "Ice cream", flavours_list)

#stand1.describe_restaurant()
#stand1.open_restaurant()
#stand1.print_flavours()


# 9-7

class Admin(User):
    def __init__(self, first_name: str, last_name: str, email: str, privileges: list):
        User.__init__(self, first_name, last_name, email)
        self.privileges: list = privileges

    def show_privileges(self):
        print(f"Admin privileges:\n","\n".join(self.privileges))

privileges_list = ["can add post", "can delete post", "can ban user", "can unban user"]
admin1 = Admin("Rick", "Astley", "RickRolled@gmail.com", privileges_list)

#admin1.describe_user()
#admin1.show_privileges()


# 9-8

class Privileges:
    def __init__(self, privileges: list):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name: str, last_name: str, email: str, privileges: list):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()

privileges_list = ["can add post", "can delete post", "can ban user", "can unban user"]

admin1 = Admin("Rick", "Astley", "RickRolled@gmail.com", privileges_list)


#admin1.describe_user()
#admin1.greet_user()
#admin1.show_privileges()


# 9-9

# Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). 
#This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default 
#battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an 
#increase in the car’s range.



# 9-10, 9-11 and 9-12 are on the file test.py


# 9-13

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


die_6 = Die(6)
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(die_6.roll_die(), end=' ')
print("\n")

die_10 = Die(10)
print("Rolling a 10-sided die 10 times:")
for _ in range(10):
    print(die_10.roll_die(), end=' ')
print("\n")

die_20 = Die(20)
print("Rolling a 20-sided die 10 times:")
for _ in range(10):
    print(die_20.roll_die(), end=' ')
print("\n")



#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from 
#the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.






#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list 
#or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times 
#the loop had to run to give you a winning ticket.




        






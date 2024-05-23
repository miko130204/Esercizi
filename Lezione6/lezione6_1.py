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


restaurant = Restaurant("La Dolce Vita", "Italian")

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

admin1.describe_user()
admin1.show_privileges()


# 9-8


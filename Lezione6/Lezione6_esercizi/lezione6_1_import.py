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





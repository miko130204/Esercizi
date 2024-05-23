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


class Admin(User):
    def __init__(self, first_name: str, last_name: str, email: str, privileges):
        User.__init__(self, first_name, last_name, email)
        self.privileges: list = Privileges(privileges)


class Privileges(Admin):
    def __init__(self, privileges: list):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin privileges:\n","\n".join(self.privileges))

privileges_list = ["can add post", "can delete post", "can ban user", "can unban user"]

admin1 = Admin("Rick", "Astley", "RickRolled@gmail.com", privileges_list)


admin1.describe_user()
admin1.greet_user()
admin1.privileges.show_privileges()

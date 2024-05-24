from user import User
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
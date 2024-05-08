class Person:

    def __init__(self, name: str, surname: str, ssn: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.ssn: str = ssn




person_1: Person = Person(name = "Miko", surname = "Mrc", ssn = "MRCMLJ04")

print(person_1.name, person_1.surname, person_1.ssn)
class Person:

    def __init__(self, name: str, surname: str, ssn: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.ssn: str = ssn

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        raise Exception("You cannot modify the name! ")
    
    def get_ssn(self):
        return self.ssn




person_1: Person = Person(name = "Miko", surname = "Mrc", ssn = "MRCMLJ04")

person_2: Person = Person(name = "Giuseppe", surname = "FFF", ssn = "BHO32")

queue: list[Person] = [person_1, person_2]

for person in queue:
    print(person.get_ssn())
from typing import Tuple

class Person:

    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:
        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender: str = gender
        self._ssn: str = self.compute_ssn()

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        raise Exception("You cannot modify the name! ")
    
    def get_ssn(self):
        return self._ssn
    
    def set_ssn(self, ssn: str):
        """
        This function set the ssn
        input: ssn : str, the parameter contains the user's ssn
        return: none
        """
        self._ssn = ssn

    def compute_ssn(self) -> bool:
        first_three_name_char = self._name[:3]
        last_three_surname_char = self._surname[-3:]
        self._ssn = first_three_name_char + last_three_surname_char
        return self._ssn



person_1: Person = Person(name = "Miko", surname = "Garbatello", birth_date = "22/10/99", birth_place = "Italy", gender = "Male")

person_2: Person = Person(name = "Giuseppe", surname = "Magliana", birth_date = "10/02/89", birth_place = "France", gender = "Man")

queue: list[Person] = [person_1, person_2]

for person in queue:
    print(person.get_ssn())
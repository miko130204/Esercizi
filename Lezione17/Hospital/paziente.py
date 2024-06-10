from persona import Persona

class Paziente(Persona):
    def __init__(self, name: str, last_name: str, age: int, idCode: str):
        super().__init__(name, last_name, age)
        
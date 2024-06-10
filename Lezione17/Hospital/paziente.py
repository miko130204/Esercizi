from persona import Persona

class Paziente(Persona):
    def __init__(self, name: str, last_name: str, age: int, idCode: str):
        super().__init__(name, last_name, age)
        self.__idCode: str = idCode
        
    def setIdCode(self, idCode: str):
        self.__idCode: str = idCode
        
    def getIdCode(self):
        return self.__idCode
    
    def patienInfo(self):
        print(f"Paziente: {self.__name} {self.__last_name}")
        print(f"ID: {self.__idCode}")
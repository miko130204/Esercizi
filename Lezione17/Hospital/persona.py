class Persona:
    def __init__(self, first_name: str, last_name: str):
        if isinstance(first_name, str):
            self.__name = first_name
        else:
            self.__name = None
            print("Il nome inserito non è una stringa!")
            
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa!")
            
        if isinstance(first_name, str) and isinstance(last_name, str):
            self.__age: int = 0
        else:
            self.__age = None

    def setName(self, first_name: str):
        self.__name = first_name

    def setLastName(self, last_name: str):
        self.__last_name = last_name

    def setAge(self, age: int):
        self.__age = age

    def getName(self):
        return self.__name

    def getLastName(self):
        return self.__last_name

    def getAge(self): 
        return self.__age

    def greet(self):
        return f"Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni!"
                
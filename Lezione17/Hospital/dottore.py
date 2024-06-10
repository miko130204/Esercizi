from persona import Persona

class Dottore(Persona):
    def __init__(self, name: str, last_name: str, age: int, specialization: str, parcel: float):
        super().__init__(name, last_name, age)
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")
            
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def getSpecialization(self): 
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.__age > 30:
            return f"Doctor {self.__name} {self.__last_name} is valid!"
        else:
            return f"Doctor {self.__name} {self.__last_name} is not valid!"
    def doctorGreet(self):
        greeting = self.greet()
        return f"{greeting} Sono un medico {self.__specialization}"
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
            
    def setSpecialization(self, specialization: str):
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")
            
    def setParcel(self, parcel: float):
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
        if self.getAge() > 30:
            return f"Doctor {self.getName()} {self.getLastName()} is valid!"
        else:
            return f"Doctor {self.getName()} {self.getLastName()} is not valid!"
        
    def doctorGreet(self):
        greeting = self.greet()
        return f"{greeting} Sono un medico {self.__specialization}"

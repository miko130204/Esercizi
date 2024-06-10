from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patients: list[Paziente], doctor: Dottore):
        self.patients: list[Paziente] = patients
        self.doctor: Dottore = doctor
        self.fatture: int = 0
        self.salary: int = 0
        
        if not doctor.isAValidDoctor():
            self.patient = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        self.salary = self.doctor.__parcel * self.fatture
        return self.salary

    def getFatture(self):
        if self.doctor and self.patient:
            self.fatture = len(self.patients)
            return self.fatture
        else:
            return 0

    def addPatient(self, newPatient: Paziente):
        if self.doctor and self.patient:
            self.patients.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor.__last_name} è stato aggiunto il paziente {newPatient.__idCode}")

    def removePatient(self, patientID):
        if self.doctor and self.patient:
            for patient in self.patients:
                if patient.__idCode == patientID:
                    self.patients.remove(patient)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.doctor.__last_name} è stato rimosso il paziente {patientID}")
                    break

import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fattura
'''
class TestPersona(unittest.TestCase):
    def setUp(self):
        self.person = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertEqual(self.person.getName(), "Mario")
        self.assertEqual(self.person.getLastname(), "Rossi")
        self.assertEqual(self.person.getAge(), 0)

    def test_set_name(self):
        self.person.setName("Luigi")
        self.assertEqual(self.person.getName(), "Luigi")

    def test_set_last_name(self):
        self.person.setLastName("Bianchi")
        self.assertEqual(self.person.getLastname(), "Bianchi")

    def test_set_age(self):
        self.person.setAge(30)
        self.assertEqual(self.person.getAge(), 30)
        
if __name__ == '__main__':
    unittest.main()
'''

'''
class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore1 = Dottore("Mario", "Rossi", 40, "Cardiologo", 100.0)
        self.dottore2 = Dottore("Luigi", "Verdi", 25, "Dermatologo", 80.0)

    def test_attributes_initialization(self):
        self.assertEqual(self.dottore1.getName(), "Mario")
        self.assertEqual(self.dottore1.getLastName(), "Rossi")
        self.assertEqual(self.dottore1.getAge(), 40)
        self.assertEqual(self.dottore1.getSpecialization(), "Cardiologo")
        self.assertEqual(self.dottore1.getParcel(), 100.0)

    def test_is_valid_doctor(self):
        self.assertTrue(self.dottore1.isAValidDoctor())
        self.assertFalse(self.dottore2.isAValidDoctor())

if __name__ == '__main__':
    unittest.main()
'''

'''
class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Mario", "Rossi", 35, "12345")

    def test_idCode_initialized_correctly(self):
        self.assertEqual(self.paziente.getIdCode(), "12345", "ID Code not initialized correctly")

    def test_name_initialized_correctly(self):
        self.assertEqual(self.paziente.getName(), "Mario", "Name not initialized correctly")

    def test_last_name_initialized_correctly(self):
        self.assertEqual(self.paziente.getLastName(), "Rossi", "Last name not initialized correctly")

if __name__ == '__main__':
    unittest.main()
'''

'''
class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Mario", "Rossi", 45, "Andrologo", 100.0)
        self.pazienti = [Paziente("John", "Doe", "123"), Paziente("Jane", "Doe", "456")]
        self.fattura = Fattura(self.pazienti, self.dottore)

    def test_initialization(self):
        self.assertEqual(self.fattura.patients, self.pazienti)
        self.assertEqual(self.fattura.doctor, self.dottore)
        self.assertEqual(self.fattura.fatture, len(self.pazienti))
        self.assertEqual(self.fattura.salary, 0)

    def test_getSalary(self):
        # Set fake values for parcel and fatture
        self.fattura.doctor.__parcel = 100
        self.fattura.fatture = 5
        self.assertEqual(self.fattura.getSalary(), 500)

    def test_getFatture(self):
        self.assertEqual(self.fattura.getFatture(), len(self.pazienti))

    def test_addPatient(self):
        new_patient = Paziente("Alice", "Smith", "789")
        self.fattura.addPatient(new_patient)
        self.assertIn(new_patient, self.fattura.patients)
        self.assertEqual(self.fattura.fatture, len(self.pazienti) + 1)

    def test_removePatient(self):
        patient_to_remove = self.pazienti[0]
        self.fattura.removePatient(patient_to_remove.__idCode)
        self.assertNotIn(patient_to_remove, self.fattura.patients)
        self.assertEqual(self.fattura.fatture, len(self.pazienti) - 1)

if __name__ == '__main__':
    unittest.main()
'''
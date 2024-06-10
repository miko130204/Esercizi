import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
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

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Mario", "Rossi", 35, "Cardiologo", 150.0)

    def test_attributes_initialization(self):
        self.assertEqual(self.dottore.getName(), "Mario")
        self.assertEqual(self.dottore.getLastName(), "Rossi")
        self.assertEqual(self.dottore.getAge(), 35)
        self.assertEqual(self.dottore.getSpecialization(), "Cardiologo")
        self.assertEqual(self.dottore.getParcel(), 150.0)

    def test_is_valid_doctor(self):
        # Test valid doctor
        self.assertEqual(self.dottore.isAValidDoctor(), "Doctor Mario Rossi is valid!")
        
        # Test invalid doctor (age less than 30)
        invalid_dottore = Dottore("Luigi", "Verdi", 25, "Dermatologo", 120.0)
        self.assertEqual(invalid_dottore.isAValidDoctor(), "Doctor Luigi Verdi is not valid!")

if __name__ == '__main__':
    unittest.main()




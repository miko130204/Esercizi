# 1

import math

def safe_sqrt(number: float):
    if number < 0:
        raise ValueError("The number can't be negative")
    return math.sqrt(number)
    
try:
    result = safe_sqrt(-4)
except ValueError as error:
    print(error)


# 2

class InvalidPasswordError(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_password(password):
    min_length = 20
    min_uppercase = 3
    min_special = 4
    special_characters = "!@#$%^&*()-_+=<>?/|\\~`"

    if len(password) < min_length:
        raise InvalidPasswordError(f"Password must be at least {min_length} characters long.")
    
    uppercase_count = sum(1 for char in password if char.isupper())
    if uppercase_count < min_uppercase:
        raise InvalidPasswordError(f"Password must contain at least {min_uppercase} uppercase characters.")
    
    special_count = sum(1 for char in password if char in special_characters)
    if special_count < min_special:
        raise InvalidPasswordError(f"Password must contain at least {min_special} special characters.")
    
    return True


try:
    validate_password("InvalidPassword123!") 
except InvalidPasswordError as error:
    print(error)

try:
    validate_password("ValidPassword123!@#%") 
    print("Password is valid.")
except InvalidPasswordError as error:
    print(error)


# 3

try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except IOError as e:
    print(f"An error occurred while handling the file: {e}")


# 4

class Date:
    def __init__(self, date_str):
        self.set_date(date_str)
    
    def set_date(self, date_str):
        day, month, year = map(int, date_str.split('.'))
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"
    
    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year
    
    def __hash__(self):
        return hash((self.day, self.month, self.year))

class DateDatabase:
    def __init__(self):
        self.dates = set()
    
    def add_date(self, date_str):
        date = Date(date_str)
        self.dates.add(date)
    
    def delete_date(self, date_str):
        date = Date(date_str)
        if date in self.dates:
            self.dates.remove(date)
        else:
            raise ValueError("Date not found in database.")
    
    def modify_date(self, old_date_str, new_date_str):
        self.delete_date(old_date_str)
        self.add_date(new_date_str)
    
    def query_date(self, date_str):
        date = Date(date_str)
        if date in self.dates:
            return date
        else:
            raise ValueError("Date not found in database.")
    
    def __str__(self):
        return '\n'.join(str(date) for date in sorted(self.dates, key=lambda d: (d.year, d.month, d.day)))

db = DateDatabase()
db.add_date("13.06.2024")
db.add_date("01.01.2023")
print("Database after adding dates:")
print(db)

db.modify_date("13.06.2024", "14.06.2024")
print("\nDatabase after modifying a date:")
print(db)

queried_date = db.query_date("14.06.2024")
print(f"\nQueried date: {queried_date}")

db.delete_date("01.01.2023")
print("\nDatabase after deleting a date:")
print(db)


# 5

class FormulaError(Exception):
    pass

def calculate(formula):
    parts = formula.split()
    
    if len(parts) != 3:
        raise FormulaError("Input does not consist of three elements.")
    
    num1, operator, num2 = parts
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise FormulaError("The first and third elements must be numbers.")
    
    if operator not in ('+', '-'):
        raise FormulaError("The operator must be '+' or '-'.")
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    
    return result

def main():
    while True:
        user_input = input("Enter a formula (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break
        
        try:
            result = calculate(user_input)
            print(f"Result: {result}")
        except FormulaError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    import unittest

    class TestCalculator(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(calculate("1 + 1"), 2.0)
        
        def test_subtraction(self):
            self.assertEqual(calculate("5 - 3"), 2.0)
        
        def test_invalid_number(self):
            with self.assertRaises(FormulaError):
                calculate("a + 1")
        
        def test_invalid_operator(self):
            with self.assertRaises(FormulaError):
                calculate("1 * 1")
        
        def test_missing_elements(self):
            with self.assertRaises(FormulaError):
                calculate("1 +")
        
        def test_too_many_elements(self):
            with self.assertRaises(FormulaError):
                calculate("1 + 1 2")
        
        def test_non_numeric_first_element(self):
            with self.assertRaises(FormulaError):
                calculate("a + 1")
        
        def test_non_numeric_second_element(self):
            with self.assertRaises(FormulaError):
                calculate("1 + b")
        
        def test_non_numeric_both_elements(self):
            with self.assertRaises(FormulaError):
                calculate("a + b")
        
        def test_large_numbers(self):
            self.assertEqual(calculate("1000000 + 2000000"), 3000000.0)
        
        def test_negative_numbers(self):
            self.assertEqual(calculate("-1 + -1"), -2.0)

    unittest.main(exit=False)
    main()


# 6



# 7
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

from fractions import Fraction
import math

class FractionError(Exception):
    pass

class NullDenominatorError(FractionError):
    def __init__(self, message="Denominator cannot be zero"):
        self.message = message
        super().__init__(self.message)

class InvalidOperationError(FractionError):
    def __init__(self, message="Invalid operation"):
        self.message = message
        super().__init__(self.message)

def create_fraction(numerator, denominator):
    try:
        if denominator == 0:
            raise NullDenominatorError()
        return Fraction(numerator, denominator)
    except NullDenominatorError as e:
        print(e)

def get_numerator(fraction):
    try:
        return fraction.numerator
    except AttributeError:
        raise InvalidOperationError("Invalid fraction object")

def get_denominator(fraction):
    try:
        return fraction.denominator
    except AttributeError:
        raise InvalidOperationError("Invalid fraction object")

def simplify_fraction(fraction):
    try:
        return fraction.limit_denominator()
    except AttributeError:
        raise InvalidOperationError("Invalid fraction object")

def add_fractions(fraction1, fraction2):
    try:
        return fraction1 + fraction2
    except TypeError:
        raise InvalidOperationError("Invalid fraction objects")

def subtract_fractions(fraction1, fraction2):
    try:
        return fraction1 - fraction2
    except TypeError:
        raise InvalidOperationError("Invalid fraction objects")

def multiply_fractions(fraction1, fraction2):
    try:
        return fraction1 * fraction2
    except TypeError:
        raise InvalidOperationError("Invalid fraction objects")

def divide_fractions(fraction1, fraction2):
    try:
        if fraction2 == 0:
            raise NullDenominatorError("Cannot divide by zero")
        return fraction1 / fraction2
    except TypeError:
        raise InvalidOperationError("Invalid fraction objects")
    except NullDenominatorError as e:
        print(e)

def are_fractions_equivalent(fraction1, fraction2):
    try:
        return fraction1 == fraction2
    except TypeError:
        raise InvalidOperationError("Invalid fraction objects")


# 7

class DataStructureIntegrityError(Exception):
    """Exception raised for errors in the data structure's integrity."""
    def __init__(self, message="Data structure integrity compromised"):
        self.message = message
        super().__init__(self.message)


class Node:
    """Node class for a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list implementation."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append an element to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, data):
        """Remove the first occurrence of data in the list."""
        if self.head is None:
            raise DataStructureIntegrityError("Cannot remove from an empty list")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            raise DataStructureIntegrityError("Element not found in the list")

        current.next = current.next.next

    def get(self, index):
        """Get the data at a specific index."""
        if self.head is None:
            raise DataStructureIntegrityError("Cannot access elements from an empty list")

        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1

        raise DataStructureIntegrityError("Index out of range")

    def print_list(self):
        """Print all elements in the list."""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def is_ordered(self):
        """Check if the list is in ascending order."""
        if self.head is None or self.head.next is None:
            return True  # An empty or single-element list is considered ordered

        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True


try:
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(8)
    linked_list.print_list()
    print("Is ordered:", linked_list.is_ordered())
    
    linked_list.remove(5)
    linked_list.print_list()
    
    linked_list.reverse()
    linked_list.print_list()
    
    print("Element at index 1:", linked_list.get(1))
except DataStructureIntegrityError as e:
    print(e)

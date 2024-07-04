import unittest

def is_valid_parenthesis(s: str) -> bool:
    possible_parenthesis = {'(': ')', '[': ']', '{':'}'}
    parenthesis_stack = []
    for char in s:
        if char in possible_parenthesis:
            parenthesis_stack.append(char)
        else:
            if not parenthesis_stack:
                return False
            val = parenthesis_stack.pop()
            if char != possible_parenthesis[val]:
                return False    
    return len(parenthesis_stack) == 0

class TestIsValidParenthesis(unittest.TestCase):
    
    def test_single_pair(self):
        self.assertTrue(is_valid_parenthesis("()"))
    
    def test_multiple_pairs(self):
        self.assertTrue(is_valid_parenthesis("()[]{}"))
    
    def test_mismatched_pair(self):
        self.assertFalse(is_valid_parenthesis("(]"))
    
    def test_wrong_nested_order(self):
        self.assertFalse(is_valid_parenthesis("([)]"))
    
    def test_correct_nested_order(self):
        self.assertTrue(is_valid_parenthesis("{[]}"))
    
    def test_empty_string(self):
        self.assertTrue(is_valid_parenthesis(""))
    
    def test_single_opening_bracket(self):
        self.assertFalse(is_valid_parenthesis("("))
    
    def test_single_closing_bracket(self):
        self.assertFalse(is_valid_parenthesis(")"))
    
    def test_long_valid_string(self):
        self.assertTrue(is_valid_parenthesis("({[]})"))
    
    def test_long_invalid_string(self):
        self.assertFalse(is_valid_parenthesis("({[})"))

if __name__ == '__main__':
    unittest.main()

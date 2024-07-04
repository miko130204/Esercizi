import unittest

def count_char(s: str):
    counter_dict = dict()
    for c in s:
        if c not in counter_dict:
            counter_dict[c] = 1
        else:
            counter_dict[c] += 1

    return counter_dict


def longest_palindrome(s: str) -> int:
    counter_dict = count_char(s)
    length = 0
    odd = False
    for val in counter_dict.values():
        if val % 2 == 0:
            length += val
        else:
            length += val - 1
            odd = True

    if odd:
        length += 1

    return length

class TestLongestPalindrome(unittest.TestCase):

    def test_1(self):
        self.assertEqual(longest_palindrome("abccccdd"), 7)

    def test_2(self):
        self.assertEqual(longest_palindrome("a"), 1)

    def test_3(self):
        self.assertEqual(longest_palindrome("Aa"), 1)

    def test_4(self):
        self.assertEqual(longest_palindrome("abccccba"), 7)

    def test_5(self):
        self.assertEqual(longest_palindrome("abcabcabc"), 7)

    def test_6(self):
        self.assertEqual(longest_palindrome(""), 0)

    def test_7(self):
        self.assertEqual(longest_palindrome("racecar"), 7)

    def test_8(self):
        self.assertEqual(longest_palindrome("aabbcc"), 6)

    def test_9(self):
        self.assertEqual(longest_palindrome("aabbccd"), 7)

    def test_10(self):
        self.assertEqual(longest_palindrome("noon"), 4)

if __name__ == "__main__":
    unittest.main()
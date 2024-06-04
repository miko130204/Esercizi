import unittest

def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t

class TestAnagram(unittest.TestCase):
    def input_file(self, filename):
        with open(filename, 'r') as f:
            s = f.readline().strip()
            t = f.readline().strip()
        return s, t

    def output_file(self, filename, result):
        with open(filename, 'w') as f:
            f.write(str(result))

    def test_case(self):
        s, t = self.input_file('test.txt')
        result = anagram(s, t)
        self.output_file('output.txt', result)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
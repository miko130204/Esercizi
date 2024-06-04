import unittest

def anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t

class TestAnagramFunction(unittest.TestCase):
    def _read_input_file(self, filename):
        with open(filename, 'r') as f:
            s = f.readline().strip()
            t = f.readline().strip()
        return s, t

    def _write_output_file(self, filename, result):
        with open(filename, 'w') as f:
            f.write(str(result))

    def test_case_1(self):
        s, t = self._read_input_file('test.txt')
        result = anagram(s, t)
        self._write_output_file('output.txt', result)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

import unittest
import os
import sys

# Ajout du chemin parent pour importer le core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.converter import SupraConverter

class TestSupraConverter(unittest.TestCase):
    def setUp(self):
        self.converter = SupraConverter()

    def test_detect_standard(self):
        line = "root@1.2.3.4 password123"
        self.assertEqual(self.converter.detect_format(line), 'standard')

    def test_detect_csv(self):
        line = "1.2.3.4,root,password123"
        self.assertEqual(self.converter.detect_format(line), 'csv')

    def test_detect_gossh(self):
        line = "1.2.3.4 host=1.2.3.4 user=root password=password123"
        self.assertEqual(self.converter.detect_format(line), 'gossh')

    def test_parse_standard(self):
        line = "root@1.2.3.4 password123"
        data = self.converter.parse_line(line, 'standard')
        self.assertEqual(data['host'], '1.2.3.4')
        self.assertEqual(data['user'], 'root')
        self.assertEqual(data['password'], 'password123')

    def test_parse_csv(self):
        line = "1.2.3.4,admin,secret"
        data = self.converter.parse_line(line, 'csv')
        self.assertEqual(data['host'], '1.2.3.4')
        self.assertEqual(data['user'], 'admin')
        self.assertEqual(data['password'], 'secret')

if __name__ == '__main__':
    unittest.main()

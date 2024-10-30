import unittest
from code_for_addition import MathClass

class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.obj = MathClass()

    def test_add(self):
        self.assertEqual(self.obj.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.obj.subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()

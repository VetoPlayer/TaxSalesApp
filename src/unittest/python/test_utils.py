import unittest

from tax.utils import round_up

class TestRoundUp(unittest.TestCase):

    def test_roundup_lower_half(self):
        self.assertEqual(round_up(5.12),5.15)

    def test_roundup_higher_half(self):
        self.assertEqual(round_up(3.18),3.2)

    def test_roundup_integer_input(self):
        self.assertEqual(round_up(3.0),3.0)

if __name__ == '__main__':
    unittest.main()

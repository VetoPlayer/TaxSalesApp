import unittest
from tax.app import *
from tax.item import Item

class TestApp(unittest.TestCase):

    def test_parse_items(self):
        exempt_dict = {'book': 'Books',
            'box of chocolates': 'Food',
            'chocolate bar': 'Food',
            'packet of headache pills': 'Drugs'}
        item_lst = ['1 book at 12.49\n']
        expected_item_lst = [Item(name="book", quantity=1, price=12.49, is_imported=False, is_exempt=True)]

        self.assertEqual(parse_items(item_lst, exempt_dict), expected_item_lst)


if __name__ == '__main__':
    unittest.main()

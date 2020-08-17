import unittest
from tax.item import Item

class TestItem(unittest.TestCase):

    def test_item_negative_quantity(self):
        self.assertRaises(AssertionError, Item, "book",-1,12.49,True,False)

    def test_item_empty_name(self):
        self.assertRaises(AssertionError, Item, "",2,12.49,True,False)

    def test_item_negative_price(self):
        self.assertRaises(AssertionError, Item, "bookshelf",2,-12.34,True,False)

    def test_item_from_dict_negative_quantity(self):
        item = {'name': 'book', 'quantity': -12, 'price': 13.46, 'imported': True}
        self.assertRaises(AssertionError, Item.from_dict, item, True)

    def test_item_from_dict_wrong_kind_price(self):
        item = {'name': 'book', 'quantity': 34, 'price': "wrong", 'imported': True}
        self.assertRaises(ValueError, Item.from_dict, item, True)

    def test_item_from_dict_empty_name(self):
        item = {'name': '', 'quantity': 67, 'price': 13.46, 'imported': True}
        self.assertRaises(AssertionError, Item.from_dict, item, True)

    def test_compute_tax_exempt_imported_item(self):
        item = {'name': 'book', 'quantity': 2, 'price': 13.46, 'imported': True}
        self.assertEqual(Item.from_dict(item, exempt=True).compute_tax(), 0.7)

    def test_compute_tax_regular_item(self):
        item = {'name': 'book', 'quantity': 2, 'price': 20.00, 'imported': False}
        self.assertEqual(Item.from_dict(item, exempt=False).compute_tax(), 2.0)

 
if __name__ == '__main__':
    unittest.main()

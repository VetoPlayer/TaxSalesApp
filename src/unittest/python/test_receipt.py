import unittest
from tax.item import Item
from tax.receipt import Receipt, sum_price, sum_tax

class TestItem(unittest.TestCase):

    def test_receipt_wrong_kind_lst(self):
        item_lst = "it_should_be_a_list_instead"
        self.assertRaises(AttributeError, Receipt, item_lst)

    def sum_tax_negative_input(self):
        item = {'name': 'book', 'quantity': 67, 'price': 13.46, 'imported': True}
        item = Item.from_dict(item, exempt=True)

        self.assertRaises(AssertionError, sum_tax, -10.4 ,item)

    def sum_price(self):
        item = {'name': 'book', 'quantity': 67, 'price': 13.46, 'imported': True}
        item = Item.from_dict(item, exempt=True)

        self.assertRaises(AssertionError, sum_price, -12.9 ,item)

    def test_compute_sum_price_actual_sum(self):
        item = {'name': 'book', 'quantity': 2, 'price': 1.0, 'imported': True}
        item = Item.from_dict(item, exempt=True)

        self.assertEqual(sum_price(10.0, item), 11.1)

    def test_compute_sum_tax_actual_sum(self):
        item = {'name': 'book', 'quantity': 2, 'price': 1.0, 'imported': True}
        item = Item.from_dict(item, exempt=True)

        self.assertEqual(sum_tax(10.0, item), 10.1)

if __name__ == '__main__':
    unittest.main()

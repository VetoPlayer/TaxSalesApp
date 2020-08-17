from tax.utils import round_up

SALE_TAX = 0.1
IMPORT_TAX = 0.05

class Item:
    """
    The Item class represents a sold item whose taxed price has to be computed.
    """
    def __init__(self, name, quantity, price, is_imported, is_exempt):
        assert(name != ""), "Name is empty"
        assert(quantity >= 1), "Invalid Quantity"
        assert(price >= 0.01), "Invalid Price"
        self.name = name
        self.quantity = quantity
        self.price = price
        self.is_imported = is_imported
        self.is_exempt = is_exempt
        self.taxed_price = self.price + self.compute_tax()

    @classmethod
    def from_dict(self, item_dict, exempt):
        return Item(
            name=item_dict['name'],
            quantity=int(item_dict['quantity']),
            price=float(item_dict['price']),
            is_imported=True if item_dict['imported'] else False,
            is_exempt=exempt)

    def compute_tax(self):
        "Computes the tax sale over the given item"
        tax = 0.0
        if not self.is_exempt:
            tax += SALE_TAX * self.price
        if self.is_imported:
            tax += IMPORT_TAX * self.price
        return round_up(tax)

    def __repr__(self):
        return "{} {}{} at {:4.2f}".format(
            self.quantity,
            "imported " if self.is_imported else "",
            self.name,
            self.price + self.compute_tax()
        )

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity and self.price == other.price and self.is_imported == other.is_imported and self.is_exempt == other.is_exempt and self.taxed_price == other.taxed_price

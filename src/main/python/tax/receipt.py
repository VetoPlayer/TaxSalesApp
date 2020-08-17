import functools

class Receipt:
    """
    The Receipt class represents a receipt, including its item list, 
    total amount of taxes to be payed 
    total price
    """
    def __init__(self, item_lst):
        self.item_lst = item_lst
        self.total_tax = functools.reduce(sum_tax, item_lst, 0)
        self.total_price = functools.reduce(sum_price, item_lst, 0)

    def __repr__(self):
        return "\n".join(list(map(str, self.item_lst))) + "\nSales Taxes: {:4.2f}\n".format(self.total_tax) + "Total: {:4.2f}".format(self.total_price)

def sum_tax(total, item):
    assert(total >=0), "Error: Computing a sum over a negative total"
    total += item.compute_tax()
    return total

def sum_price(total, item):
    assert(total >=0), "Error: Computing a sum over a negative total"
    total += item.taxed_price
    return total



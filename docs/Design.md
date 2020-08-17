## Design Choices

This implementation follows design choices involving the following reasonable assumptions:

* The number of different items sold by a given shop can be significant: for this reason the application reads the exempted list of items from an input file and uses a dictionary, allowing for a fast lookup on whether a given item is tax-exempted or not. 
* As in real life, the item price reported at the end of each line is assumed to represent the total price for the listed item rather than the price for a single product.
* As in real life, the input receipt is not expected to list products of the same kind on different lines.


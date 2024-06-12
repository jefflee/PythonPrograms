from Product import Product


"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

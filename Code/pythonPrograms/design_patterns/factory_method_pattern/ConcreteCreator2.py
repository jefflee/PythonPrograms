from Creator import Creator
from Product import Product
from ConcreteProduct2 import ConcreteProduct2


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

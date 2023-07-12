import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def test_coffee_shop_has_name(self):
        coffee_shop = CoffeeShop("The Prancing Pony",0)
        self.assertEqual("The Prancing Pony", coffee_shop.name)

    def test_coffee_shop_has_till(self):
        coffee_shop = CoffeeShop("The Prancing Pony", 100)
        expected = 100
        actual = coffee_shop.till
        self.assertAlmostEqual(expected, actual)
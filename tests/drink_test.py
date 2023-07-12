import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Vanilla mocha cappuchino flatte", 4)

    def test_coffee_shop_has_name(self):
        self.assertEqual("Different", self.drink.name)


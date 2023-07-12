import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Vanilla mocha cappuchino flatte", 4)

    def test_drink_has_name(self):
        self.assertEqual("Vanilla mocha cappuchino flatte", self.drink.name)

    
    def test_drink_has_price(self):
        self.assertEqual(4.0, self.drink.price)


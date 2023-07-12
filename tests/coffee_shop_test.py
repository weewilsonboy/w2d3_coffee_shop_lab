import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony",100)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_coffee_shop_has_till(self): #make a test, the name implies it will check that there is a till
        expected = 100 #the number we expect to be as coffee_shop.till
        actual = self.coffee_shop.till #what coffee_shop.till actually is
        self.assertAlmostEqual(expected, actual) #check that the actual is the same as expected

    def test_coffee_shop_increase_till(self):
        self.coffee_shop.increase_till(2.5)
        self.assertEqual(102.5, self.coffee_shop.till)
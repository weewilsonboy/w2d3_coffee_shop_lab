import unittest
from src.customer import Customer
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Kev", 3)
        self.shop = CoffeeShop("The Prancing Pony",100)
    
    def test_has_name(self):
        self.assertEqual("Kev", self.customer.name)
    
    def test_has_wallet(self):
        self.assertEqual(3, self.customer.wallet)

    def test_wallet_reduce(self):
        self.customer.wallet_reduce(2)
        self.assertEqual(1, self.customer.wallet)
    
    def test_buy(self):
        self.shop.add_drink("Mocha", 5)
        self.customer.buy("Mocha", self.shop)
        self.assertEqual(95, self.shop.till)
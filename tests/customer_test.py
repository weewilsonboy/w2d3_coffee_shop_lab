import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Kev", 3)
    
    def test_has_name(self):
        self.assertEqual("Kev", self.customer.name)
    
    def test_has_wallet(self):
        self.assertEqual(3, self.customer.wallet)

    def test_wallet_reduce(self):
        self.customer.wallet_reduce(2)
        self.assertEqual(1, self.customer.wallet)
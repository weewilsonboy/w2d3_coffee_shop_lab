import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Kev", 3)
    
    def test_has_name(self):
        self.assertEqual("Kev", self.customer.name)
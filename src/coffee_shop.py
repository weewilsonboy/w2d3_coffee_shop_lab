from src.drink import Drink

class CoffeeShop:
	
	def __init__(self, name, till):
		self.name=name
		self.till = till
		self.drinks_stock = {}
		self.drinks_menu = []

	def increase_till(self, amount):
		self.till += amount

	def decrease_till(self, amount):
		if amount < self.till:
			self.till -= amount
		else:
			print("Not enough money in till")
	
	def add_drink(self, drink_name, drink_price):

		if drink_name not in self.drinks_stock.keys():
			self.drinks_menu.append(Drink(drink_name, drink_price))
			self.drinks_stock[drink_name] = 1
		else:
			self.drinks_stock[drink_name] += 1
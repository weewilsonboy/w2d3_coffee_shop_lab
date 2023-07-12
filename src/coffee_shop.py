class CoffeeShop:
	
	def __init__(self, name, till):
		self.name=name
		self.till = till
		self.drinks =[]

	def increase_till(self, amount):
		self.till += amount

	def decrease_till(self, amount):
		if amount < self.till:
			self.till -= amount
		else:
			print("Not enough money in till")

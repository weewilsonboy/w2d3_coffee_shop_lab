class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def wallet_reduce(self, amount):
        self.wallet -= amount

    def buy(self, drink_name, shop):
        bought_drink = shop.sell_drink(drink_name)
        self.wallet_reduce(bought_drink.return_price())


class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def wallet_reduce(self, amount):
        self.wallet -= amount




class Category:
    def __init__(self, name):
        self.categoryName = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False

    def get_balance(self):
        balance = 0
        for transac in self.ledger:
            balance += transac.get("amount")
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.categoryName}")
            category.deposit(amount, f"Transfer from {self.categoryName}")
            return True
        return False
    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False


def create_spend_chart(categories):
    pass


food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
print("food.ledger[2]:", food.ledger[2])
print("entertainment.ledger[0]:", entertainment.ledger[0])

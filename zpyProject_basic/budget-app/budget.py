# https://realpython.com/python-f-strings/
# https://realpython.com/python-formatted-output/
# https://www.delftstack.com/howto/python/split-string-to-a-list-of-characters/
# https://stackoverflow.com/questions/30902558/finding-length-of-the-longest-list-in-an-irregular-list-of-lists
# https://stackoverflow.com/questions/6076270/lambda-function-in-list-comprehensions/6076304
# DO NOT USE LAMBDA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# https://stackoverflow.com/questions/22895791/python-code-for-sum-with-condition/22895828


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
        # balance = 0
        # for transac in self.ledger:
        #     balance += transac.get("amount")
        # return balance
        return sum(transac.get("amount") for transac in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.categoryName}")
            category.deposit(amount, f"Transfer from {self.categoryName}")
            return True
        return False

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False

    def get_all_withdraw(self):
        withdraw_Transac = [transac for transac in self.ledger if transac["amount"] < 0]
        withdraw_Total = 0
        for transac in withdraw_Transac:
            withdraw_Total += transac["amount"]
        return withdraw_Transac + [{"Total": withdraw_Total}]

    def __str__(self):
        headerStr = f"{self.categoryName:*^30}\n"
        transacStr = ""
        for item in self.ledger:
            transacStr += f"{item['description']:23.23s}{item['amount']:>7.2f}\n"
        totalStr = f"Total: {self.get_balance()}"
        return "".join((headerStr, transacStr, totalStr))


def create_spend_chart(categories):
    chart_header = "Percentage spent by category\n"
    chart_column = create_chart_column(categories)
    chart_footer = create_footer_chart(categories)
    return "".join((chart_header, chart_column, chart_footer))


def create_footer_chart(categories):
    chart_footer = " " * 4 + "-" * (1 + 3 * len(categories)) + "\n"
    categories_Name = [list(category.categoryName) for category in categories]
    max_char = max(len(name) for name in categories_Name)
    categories_Char = [
        (name + [" "] * (max_char - len(name))) for name in categories_Name
    ]
    for index in range(max_char):
        line = " " * 5
        for char_name in categories_Char:
            line += char_name[index] + "  "
        chart_footer += line + "\n"
    return chart_footer[:-1]


def create_chart_column(categories):
    chart_display = ""
    withdraw_categories = [total_withdraw(category) for category in categories]
    withdraw_categories_percent = [
        int((x * 10) // sum(withdraw_categories)) for x in withdraw_categories
    ]
    column_categories = [
        [" "] * (10 - percent) + ["o"] * (percent + 1)
        for percent in withdraw_categories_percent
    ]
    for index in range(0, 11, 1):
        chart_display += (
            f"{(10-index) * 10 :>3}| "
            + "".join(f"{column[index]}  " for column in column_categories)
            + "\n"
        )
        # for column in column_categories:
        #     chart_display += f"{column[index]}  "
        # chart_display += "\n"
    return chart_display


def total_withdraw(category):
    return sum(
        transac["amount"] for transac in category.ledger if transac["amount"] < 0
    )


food = Category("Food")
entertainment = Category("Entertainment")
# business = Category("Business")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)

divide_chart = (
    f"100|          \n"
    f" 90|          \n"
    f" 80|          \n"
    f" 70|    o     \n"
    f" 60|    o     \n"
    f" 50|    o     \n"
    f" 40|    o     \n"
    f" 30|    o     \n"
    f" 20|    o  o  \n"
    f" 10|    o  o  \n"
    f"  0| o  o  o  \n"
)

expectedChart = (
    f"Percentage spent by category\n"
    f"100|          \n"
    f" 90|          \n"
    f" 80|          \n"
    f" 70|    o     \n"
    f" 60|    o     \n"
    f" 50|    o     \n"
    f" 40|    o     \n"
    f" 30|    o     \n"
    f" 20|    o  o  \n"
    f" 10|    o  o  \n"
    f"  0| o  o  o  \n"
    f"    ----------\n"
    f"     B  F  E  \n"
    f"     u  o  n  \n"
    f"     s  o  t  \n"
    f"     i  d  e  \n"
    f"     n     r  \n"
    f"     e     t  \n"
    f"     s     a  \n"
    f"     s     i  \n"
    f"           n  \n"
    f"           m  \n"
    f"           e  \n"
    f"           n  \n"
    f"           t  "
)

expectedStr = (
    f"*************Food*************\n"
    f"deposit                 900.00\n"
    f"milk, cereal, eggs, bac -45.67\n"
    f"Transfer to Entertainme -20.00\n"
    f"Total: 834.33"
)

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
# business.withdraw(10.99)

# ================================================
chart_input = [food, entertainment]
chart_created = create_spend_chart(chart_input)
# ================================================
print("chart_created:\n" + chart_created)
# print("divide_chart:\n" + divide_chart)
# print(food.get_all_withdraw())
# print(entertainment.get_all_withdraw())
# print(business.get_all_withdraw())
create_chart_column(chart_input)
# The percentage spent should be calculated only with withdrawals and not with deposits.
# "o" character.
# The height of each bar should be rounded down to the nearest 10.
# The horizontal line below the bars should go two spaces past the final bar.
# This function will be tested with up to four categories.

expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
# print(expected)

# arr = [7, 2, 1]
# convert_percent_arr(arr)
# print("convert_percent_arr(arr):", convert_percent_arr(arr))

class MoneyMachine:
    """Money Machine Class"""

    COINS = {"Quarter": 0.25, "Dime": 0.10, "Nickle": 0.05, "Pennie": 0.01}

    def __init__(self):
        self.money = 0

    def print_report(self):
        money = "{:.2f}".format(self.money)
        print("Money Machine Report")
        print(f"Money: ${money}\n")

    def process_payment(self, price, amount_paid):
        """Return change and Add profit"""
        change = amount_paid - price
        if change < 0:
            print("Sorry that's not enough money. Money refunded.\n")
            return False
        elif change > 0:
            change = "{:.2f}".format(change)
            print("Thank you.")
            print(f"Here is ${change} in change.")
            self.money += price
        else:
            print("Thank you.")
            self.money += price

        return True

    def insert_coins(self, price):
        """Insert coins into machine"""
        amount_paid = 0
        print("Please insert coins.")
        for coin in self.COINS:
            amount_paid += int(input(f"How many {coin}s?: ")) * self.COINS[coin]

        change = self.process_payment(price, amount_paid)

        return change

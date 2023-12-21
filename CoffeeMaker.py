# Day 15
class CoffeeMaker:
    def __init__(self):
        """Initialize Coffee Maker"""
        # Drink: Water: ml, Coffee: g, Milk: ml, Price: $
        self.hot_drinks = {
            "Espresso": {"Water": 50, "Coffee": 18, "Milk": 0, "Price": 1.50},
            "Latte": {"Water": 200, "Coffee": 24, "Milk": 150, "Price": 2.50},
            "Cappuccino": {"Water": 250, "Coffee": 24, "Milk": 100, "Price": 3.00},
        }
        # Resources = Water: ml, Coffee: g, Milk: ml, Money: $
        self.resources = {"Water": 300, "Coffee": 100, "Milk": 200, "Money": 0}

    def print_report(self):
        """Resources = Water: ml, Coffee: g, Milk: ml, Money: $"""
        resources = self.resources
        print(f"Water: {resources['Water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g")
        print(f"Money: ${resources['Money']}")
        print()
        return

    def enough_resources(self, drink):
        """Check if the machine has enough resources to make a drink"""
        resources = self.resources
        ingredients = self.hot_drinks[drink]
        is_enough_resources = True
        for ingredient in resources:
            if ingredient == "Money":
                break
            if resources[ingredient] < ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                is_enough_resources = False

        return is_enough_resources

    def add_profit(self, profit):
        self.resources["Money"] += profit
        return

    def process_payment(self, price, quarters, dimes, nickles, pennies):
        """Return change and Add profit"""
        amount_paid = (
            (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        )
        change = amount_paid - price
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif change > 0:
            change = "{:.2f}".format(change)
            print("Thank you.")
            print(f"Here is ${change} in change.")
            self.add_profit(price)
        else:
            print("Thank you.")
            self.add_profit(price)

        return True

    def insert_coins(self, drink):
        """Insert coins into machine"""
        price = self.hot_drinks[drink]["Price"]
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        successful_payment = self.process_payment(
            price, quarters, dimes, nickles, pennies
        )
        return successful_payment

    def make_drink(self, drink):
        """Make the drink"""
        ingredients = self.hot_drinks[drink]
        for resource in self.resources:
            if resource == "Money":
                break
            self.resources[resource] -= ingredients[resource]
        return


def main():
    coffee_maker = CoffeeMaker()

    while True:
        drink = input("What would you like? (espresso/latte/cappuccino):\n").title()
        if drink == "Off":
            print("Powering Off")
            break
        if drink == "Report":
            coffee_maker.print_report()
            continue
        if not coffee_maker.enough_resources(drink):
            print(f"Sorry, can't make {drink}.")
            continue
        if not coffee_maker.insert_coins(drink):
            continue

        coffee_maker.make_drink(drink)
        print(f"Here is your {drink}. Enjoy!\n")


if __name__ == "__main__":
    main()

# Day 15 / Day 16
class CoffeeMaker:
    """Coffee Maker Class"""

    def __init__(self):
        """Initialize Coffee Maker"""
        # Resources = Water: ml, Coffee: g, Milk: ml
        self.resources = {"Water": 300, "Coffee": 100, "Milk": 200}

    def print_report(self):
        """Resources = Water: ml, Coffee: g, Milk: ml, Money: $"""
        resources = self.resources
        print("Coffee Maker Report")
        print(f"Water: {resources['Water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g\n")

    def enough_resources(self, drink):
        """Check if the machine has enough resources to make a drink"""
        resources = self.resources
        ingredients = drink.ingredients
        is_enough_resources = True
        for ingredient in resources:
            if resources[ingredient] < ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                is_enough_resources = False

        return is_enough_resources

    def make_drink(self, drink):
        """Make the drink"""
        ingredients = drink.ingredients
        for resource in self.resources:
            self.resources[resource] -= ingredients[resource]
        print(f"Here is your {drink.name}. Enjoy!\n")

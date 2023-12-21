"""Main Program for Operating on Coffee Machine and Processing Money"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}):\n").title()
        if choice == "Off":
            print("Powering Off")
            break
        if choice == "Report":
            coffee_maker.print_report()
            money_machine.print_report()
            continue

        drink = menu.find_drink(choice)
        if drink is None:
            continue
        if not coffee_maker.enough_resources(drink):
            print(f"Sorry, can't make {choice}.")
            continue
        if not money_machine.insert_coins(drink.cost):
            continue

        coffee_maker.make_drink(drink)


if __name__ == "__main__":
    main()

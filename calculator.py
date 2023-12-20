# Day 10
LOGO = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1**num2


def main():
    print(LOGO)
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "^": power}
    continue_program = True
    answer = 0
    while continue_program:
        print("What's the first number?")
        num1 = input("Type 'ans' to set as previous answer.\n")
        if num1 == "ans":
            num1 = answer
        else:
            num1 = float(num1)

        print()
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the lines above\n")
        calculation_function = operations[operation_symbol]
        print()

        print("What's the second number?")
        num2 = input("Type 'ans' to set as previous answer.\n")
        if num2 == "ans":
            num2 = answer
        else:
            num2 = float(num2)

        answer = calculation_function(num1, num2)

        print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")

        result = input("Continue calculating? 'Yes' or 'No'\n").lower()
        if result == "no":
            continue_program = False

    print("Goodbye.")


if __name__ == "__main__":
    main()

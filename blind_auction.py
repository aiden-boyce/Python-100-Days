# Day 9
from os import system, name

LOGO = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


# Clear The Screen
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def find_highest_bidder(all_bids):
    winner = ""
    highest_bid = 0
    for bidder, bid in all_bids.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder

    return winner


def main():
    print(LOGO)
    print("Welcome to the Secret Auction Program.")
    continue_program = True
    all_bids = {}
    while continue_program:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        all_bids[name] = bid
        other_bidders = input("Are there any other bidders? 'Yes' or 'No': ").lower()
        continue_program = other_bidders == "yes"
        clear()

    winner = find_highest_bidder(all_bids)
    print(f"The winner is {winner} with a bid of ${all_bids[winner]}.")


if __name__ == "__main__":
    main()

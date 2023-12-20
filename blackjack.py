# Day 11
from os import system, name
from random import choice


LOGO = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


# Clear The Screen
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(hand):
    has_ace = False
    score = 0
    for card in hand:
        if card == 11:
            has_ace = True
        score += card
    # If hand has an ace and > 21, set Ace = 1
    if has_ace and score > 21:
        score -= 10
        i = hand.index(11)
        hand[i] = 1

    return score


def compare_scores(players_score, dealers_score):
    if players_score == dealers_score:
        print("It's a draw!")
        return 0
    elif players_score == 21:
        print("You won with a Blackjack!")
        return 1
    elif dealers_score == 21:
        print("Dealer won with a Blackjack!")
        return -1
    elif players_score > 21:
        print("You lose!")
        return -1
    elif dealers_score > 21:
        print("You won!")
        return 1
    elif players_score > dealers_score:
        print("You won!")
        return 1
    else:
        print("You lose!")
        return -1


def play_game():
    players_hand = []
    dealers_hand = []
    # Player and Dealer start with two cards
    for _ in range(2):
        players_hand.append(deal_card())
        dealers_hand.append(deal_card())

    players_score = 0
    dealers_score = 0

    player_continues = True
    while True:
        print()
        players_score = calculate_score(players_hand)
        # Game Over if Player or Dealer > 21
        if players_score > 21 or dealers_score > 21:
            break

        print(f"Your cards: {players_hand}")
        print(f"Your score: {players_score}")

        dealers_score = calculate_score(dealers_hand)

        if player_continues:
            print(f"Dealer's First Card: {dealers_hand[0]}")
        elif not player_continues and dealers_score >= 17:
            print(f"Dealer's Cards: {dealers_hand}")
            print(f"Dealer's Score: {dealers_score}")
            break
        # Dealer draws until their score is greater than 17
        elif not player_continues and dealers_score < 17:
            print(f"Dealer's Cards: {dealers_hand}")
            print(f"Dealer's Score: {dealers_score}")
            dealers_hand.append(deal_card())

        # Check for Blackjack
        if players_score == 21 or dealers_score == 21:
            break

        # Check if player already said stand
        if player_continues:
            result = input("Would you like to hit or stand? 'Hit' or 'Stand'\n").lower()

        if result == "stand":
            player_continues = False
        elif result == "hit":
            player_continues = True
            players_hand.append(deal_card())

    print()
    players_score = calculate_score(players_hand)
    dealers_score = calculate_score(dealers_hand)
    print(f"Your cards: {players_hand}")
    print(f"Your score: {players_score}")
    print(f"Dealer's Cards: {dealers_hand}")
    print(f"Dealer's Score: {dealers_score}")

    return compare_scores(players_score, dealers_score)


def main():
    # Ace = 11, Face Cards = 10
    player_wins = 0
    dealer_wins = 0
    while True:
        clear()
        print(LOGO)
        result = play_game()
        if result == 1:
            player_wins += 1
        elif result == -1:
            dealer_wins += 1

        print()
        print(f"Player Wins: {player_wins}")
        print(f"Dealer Wins: {dealer_wins}")

        result = input("Would you like to continue playing? 'Yes' or 'No'\n").lower()
        if result == "no":
            break

    print("Goodbye.")


if __name__ == "__main__":
    main()

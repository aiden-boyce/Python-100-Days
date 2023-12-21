# Day 14
from random import choice
from game_data import logo, data, vs


def get_competitor():
    """Get competitor from data"""
    competitor = choice(data)
    return competitor


def get_competitor_info(competitor, num):
    """Print all info about competitor and return their follower count"""
    name = competitor["name"]
    description = competitor["description"]
    country = competitor["country"]
    follower_count = competitor["follower_count"]
    print(f"Compare {num}: {name}, a {description}, from {country}.")
    return follower_count


def play_game(prev_competitor):
    """Play Higher or Lower"""
    # Competitor A = Prev Competitor if there was one or a New Competitor
    competitor_a = prev_competitor or get_competitor()
    competitor_b = get_competitor()
    # Make sure its not same competitor
    while competitor_a == competitor_b:
        competitor_b = get_competitor()

    competitor_a_followers = get_competitor_info(competitor_a, "A")
    print(vs)
    competitor_b_followers = get_competitor_info(competitor_b, "B")

    guess = input("Who has more followers? Type 'A' or 'B':\n").lower()
    if guess == "a" and competitor_a_followers >= competitor_b_followers:
        print("Correct!")
        return 1, competitor_a
    elif guess == "b" and competitor_b_followers >= competitor_a_followers:
        print("Correct!")
        return 1, competitor_b

    print("Wrong!")
    return 0, 0


def main():
    print(logo)
    continue_game = True
    competitor = None
    wins = 0
    while continue_game:
        print(f"\nCurrent Score: {wins}")
        result, competitor = play_game(competitor)

        if result == 1:
            wins += 1
        else:
            print("You lost.")
            break

    print(f"\nFinal Score: {wins}")
    print("Goodbye.")


if __name__ == "__main__":
    main()

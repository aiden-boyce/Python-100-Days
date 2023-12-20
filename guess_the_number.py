# Day 12
from random import randint

LOGO = """
   ___                       _   _                __                 _               
  / _ \_   _  ___  ___ ___  | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                     
"""
RAND_NUM = randint(1, 100)


def set_difficulty():
    result = input("Choose a difficulty. Type 'easy' or 'hard'.\n")
    if result == "easy":
        return 10
    else:
        return 5


def higher_or_lower(guess):
    if guess == RAND_NUM:
        print(f"You got it! The answer was {RAND_NUM}.")
        return 0
    elif guess < RAND_NUM:
        print("Too low.")
        return -1
    else:
        print("Too high.")
        return 1


def main():
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    lives = set_difficulty()
    while lives > 0:
        print(f"You have {lives} lives.")
        guess = int(input("Guess a number:\n"))
        result = higher_or_lower(guess)
        if result == 0:
            break
        else:
            lives -= 1

    if lives != 0:
        print("You won!")
    else:
        print("You lost.")
    print("Goodbye.")


if __name__ == "__main__":
    main()

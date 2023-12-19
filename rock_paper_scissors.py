# Day 4
from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
rock_paper_scissors = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors!")
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
)

if user_choice < 0 or user_choice > 2:
    print("Invalid number.")
    exit()

print(rock_paper_scissors[user_choice])
computer_choice = randint(0, 2)
print("Computer chose: ")
print(rock_paper_scissors[computer_choice])

if user_choice == computer_choice:
    print("It's a draw.")
    exit()

match user_choice:
    case 0:
        if computer_choice == 1:
            print("You lose.")
        else:
            print("You win!")
    case 1:
        if computer_choice == 0:
            print("You win!")
        else:
            print("You lose.")
    case 2:
        if computer_choice == 0:
            print("You lose.")
        else:
            print("You win!")

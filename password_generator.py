# Day 5
from random import choice, shuffle

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters do you want in your password?\n"))
num_numbers = int(input("How many numbers do you want in your password?\n"))
num_symbols = int(input("How many symbols do you want in your password?\n"))

easy_password = []

i = 0
while i < num_letters:
    easy_password.append(choice(letters))
    i += 1
i = 0
while i < num_numbers:
    easy_password.append(choice(numbers))
    i += 1
i = 0
while i < num_symbols:
    easy_password.append(choice(symbols))
    i += 1

hard_password = easy_password.copy()
easy_password = "".join(easy_password)

# Randomize Order instead of Sequential
shuffle(hard_password)
hard_password = "".join(hard_password)

print(f"Your easy password is:\n{easy_password}")
print(f"Your hard password is:\n{hard_password}")

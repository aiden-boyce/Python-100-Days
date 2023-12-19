# Day 7
from random import choice
from hangman_features import stages, word_list, logo


def get_random_word():
    words = word_list
    chosen_word = choice(words)
    return chosen_word


def print_current_stage(guessed_word, guessed_letters, stage):
    print(stage)
    print(f"Guess Display: {guessed_word}")
    print(f"Guessed Letters: {guessed_letters}")


def is_word_correct(guessed_word):
    return not "_" in guessed_word


def add_letter(guess, guessed_word, chosen_word):
    for i, letter in enumerate(chosen_word):
        if guess == letter:
            guessed_word[i] = guess
    return guessed_word


def main():
    hangman_logo = logo
    print(hangman_logo)
    chosen_word = get_random_word()
    # Blank word
    guessed_word = ["_" for letter in chosen_word]
    stage_list = stages
    lives = len(stage_list) - 1
    guessed_letters = []
    game_over = False
    # Play until game over
    while not game_over:
        print_current_stage(guessed_word, guessed_letters, stage_list[lives])
        guess = input("Guess a letter:\n").lower()

        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        correct_guess = guess in chosen_word
        guessed_letters.append(guess)
        if correct_guess:
            guessed_word = add_letter(guess, guessed_word, chosen_word)
            print("Right!")
        else:
            print("Wrong.")
            lives -= 1

        game_over = lives == 0 or is_word_correct(guessed_word)

    print()
    if lives > 0:
        print("Congratulations you won!")
    else:
        print("You lost!")

    print(f"The word was:\n{chosen_word}\n")
    print("Game Over!")


if __name__ == "__main__":
    main()

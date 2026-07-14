"""
Simple Text-Based Hangman Game
--------------------------------
- 5 predefined words
- Max 6 incorrect guesses
- Console input/output only
"""

import random

WORDS = ["bhavesh","sugandhan"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
       -----
       |   |
       |
       |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |   |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  /
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    ---------
    """,
]


def choose_word(word_list):
    """Pick a random word from the list."""
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_guess(guessed_letters):
    """Prompt the player for a single valid letter guess."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        # Loop completed without breaking -> player lost
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Game over! You've run out of guesses.")
        print(f"The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
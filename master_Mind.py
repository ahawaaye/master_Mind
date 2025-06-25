#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
import random

print("MasterMind")

COLORS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']


def generate_Code(length=4, words=COLORS):
    return [str(random.choice(words)) for _ in range(length)]


def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))

    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(
        min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts
    )

    return black_Pegs, white_Pegs


def show_Secret(mystery):
    print(mystery)


def play_Mastermind():
    print("Welcome to Mastermind!")
    print(
        "Guess the 4-color code. Available colors are:"
        " red, yellow, orange, green, blue, purple."
    )
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = []
        valid_Guess = False
        while not valid_Guess:
            user_input = input(f"Attempt {attempt}: ").strip().lower()
            guess = user_input.split()
            valid_Guess = len(guess) == 4 and all(color in COLORS for color in guess)
            if not valid_Guess:
                print(
                    "Invalid input. Please enter 4 colors from the list:"
                    " red, yellow, orange, green, blue, purple."
                )

        black, white = get_Feedback(secret_Code, guess)
        print(
            f"Black pegs (correct position): {black},"
            f" White pegs (wrong position): {white}"
        )

        if black == 4:
            print(f"Congratulations! You guessed the code: {' '.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {' '.join(secret_Code)}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N)? ").upper()

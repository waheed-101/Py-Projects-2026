"""
Number Guessing Game
Player has 7 attempts to guess a random number between 1-99.
"""

import random


number = random.randrange(1, 100)
guess_number = int(input("Enter the Number: "))
attempt = 7

while attempt > 0:
    if guess_number == number:
        print(f"\nYou guessed it right!\nGuess Number: {number}")
        break

    if guess_number > number:
        print("Too High")
    elif guess_number < number:
        print("Too Low")

    attempt -= 1

    if attempt > 0:
        print(f"Remaining Attempts: {attempt}")
        guess_number = int(input("\nEnter Number Again: "))
    else:
        print(f"Game Over! The Number was: {number}")
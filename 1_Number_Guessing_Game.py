
import random

number = random.randrange(1, 100)
guess_number = int(input("Enter the Number: "))
attempt = 7

while attempt > 0:
    if guess_number > number:
        print("Too High")
        print(f"Remaining Attempt: {attempt - 1}")
        guess_number = int(input("\nEnter Number Again: "))
        attempt -= 1

    elif guess_number < number:
        print("Too Low")
        print(f"Remaining Attempt: {attempt - 1}")
        guess_number = int(input("\nEnter Number Again: "))
        attempt -= 1

    else:
        print(f"\n*** You guessed it right. ***\nGuess Number: {number}")
        break


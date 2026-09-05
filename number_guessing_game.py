# CodeOrbit Tech - Python Programming Internship
# Task : Number Guessing Game

import random


def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Keep track of the number of attempts
    attempts = 0

    print("\n===== Number Guessing Game =====")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            # Take the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("\n🎉 Congratulations! You guessed the number!")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        play_game()

        # Ask if the user wants another round
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing! 👋")
            break


# Start the game
main()
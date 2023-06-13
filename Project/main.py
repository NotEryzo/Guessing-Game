# Guessing game using OOP by Sami

import random

# Class function with constructor and parameters.
class GuessingGame:
    def __init__(self, attempts, difficulty):
        self.attempts = attempts
        self.number = random.randint(1, difficulty)

    def playgame(self):
        print("\nWelcome to Guess the Number!")
        print(f"I am thinking of a number between 1 and {difficulty}. You have {self.attempts} attempts to guess.")

        # Gets the user's number and checks if the number is correct.
        attempts = 0
        while attempts < self.attempts:
            guess = self.getplayerguess()
            result = self.checkguess(guess)

            if result == "correct":
                print("Congratulations! You guessed the correct number!")
                return
            elif result == "high":
                print("The number is higher than your guess.")
            else:
                print("The number is lower than your guess.")

            attempts += 1

        print("\nGame over! You ran out of attempts.")
        print(f"I was thinking of the number: {self.number}")

    def getplayerguess(self):
        while True:
            guess = input("Enter your guess: ")
            if guess.isdigit():
                guess = int(guess)
                if 1 <= guess <= difficulty:
                    return guess
                else:
                    print(f"Invalid input! Please enter a number between 1 and {difficulty}.")
            else:
                print("Invalid input! Please enter a valid number.")

    def checkguess(self, guess):
        if guess == self.number:
            return "correct"
        elif guess < self.number:
            return "high"
        else:
            return "low"

# Difficulty menu where user is able to choose the difficulty
def selectdifficulty():
    print("Select the difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        return 50
    elif choice == "2":
        return 100
    elif choice == "3":
        return 500
    else:
        print("Invalid choice. Please try again.")
        return selectdifficulty()

# Get the chosen difficulty level from the player
difficulty = selectdifficulty()

# Set the number of attempts based on the chosen difficulty
if difficulty == 50:
    attempts = 10
elif difficulty == 100:
    attempts = 7
elif difficulty == 500:
    attempts = 3

# Creates a game variable with a certain amount of attempts and a certain difficulty. 
game = GuessingGame(attempts, difficulty)

# Start the game
game.playgame()

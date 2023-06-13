# Guessing game using OOP by Sami

import random 

# Class function with constructor and parameters.
class GuessingGame:
    def __init__(self, attempts):
        self.attempts = attempts
        self.number = random.randint(1, 50) # Random number between 1 - 50.
    
    def playgame(self):
        print("Welcome to Guess the Number!")
        print(f"I am thinking of a number between 1 and 50. You have {self.attempts} attempts to guess.")
        
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

        print("Game over! You ran out of attempts.")
        print(f"I was thinking of the number: {self.number}")

    def getplayerguess(self):
        while True:
            guess = input("Enter your guess: ")
            if guess.isdigit():
                guess = int(guess)
                if 1 <= guess <= 50:
                    return guess
                else:
                    print("Invalid input! Please enter a number between 1 and 50.")
            else:
                print("Invalid input! Please enter a valid number.")


    def checkguess(self, guess):
        if guess == self.number:
            return "correct"
        elif guess < self.number:
            return "high"
        else:
            return "low"


# Allows the game to give 5 attempts. 
game = GuessingGame(5)
game.playgame()

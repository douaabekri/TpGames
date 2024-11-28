import random

class Guess:
    total_points = 0  

    @staticmethod
    def GameGuess():
        Randomint = random.randint(1, 10)  
        attempts = 5
        print("Guess a number from 1 to 10! You only have 5 chances!")

        for i in range(attempts):
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 10:
                print("Wrong number! Please choose a number between 1 and 10.")
                continue  
            
            if guess == Randomint:
                print("Correct! You guessed the right number!")
                Guess.total_points += 10
                print(f"You earned 10 points! Total points: {Guess.total_points}")
                return
            elif guess < Randomint:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
            
            remaining_attempts = attempts - i - 1
            if remaining_attempts > 0:
                print(f"You still have {remaining_attempts} attempts.")
        
        print(f"Sorry, the correct number was {Randomint}.")
        print(f"Total points: {Guess.total_points}")

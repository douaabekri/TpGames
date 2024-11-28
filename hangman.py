import random

class Hangman:
    total_points = 0 

    @staticmethod
    def Gamehangman():
        print("_________|| Hangman Game ||_________")
        words = ['canada', 'italy', 'brazil', 'algeria', 'iran', 'spain', 'morocco', 'egypt', 'tunisia', 'iraq', 'libya']
        word = random.choice(words).lower()
        guessed_word = ['_'] * len(word)
        attempts = 6
        guessed_letters = []

        print("Welcome to Hangman!")
        print("Guess the word:", ' '.join(guessed_word))

        while attempts > 0:
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
                continue

            if guess in guessed_letters:
                print(f"You've already guessed the letter '{guess}'. Try a different letter.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
                print("Good job! The word now looks like this:", ' '.join(guessed_word))
            else:
                attempts -= 1
                print(f"Incorrect guess. You have {attempts} attempts left.")

            if '_' not in guessed_word:
                print("Congratulations! You've guessed the word:", word)
                Hangman.total_points += 10
                print(f"You earned 10 points! Total points: {Hangman.total_points}")
                return

        print("Game over! You've run out of attempts.")
        print(f"The word was: {word}")
        print(f"Total points: {Hangman.total_points}")

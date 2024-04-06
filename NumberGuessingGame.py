'''
                    NUMBER GUESSING GAME - PYTHON 

'''
import random

print("Welcome to the Guess the Number Game!")
print("I've selected a number between 1 and 10. Can you guess it?")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
print(secret_number)
# Number of attempts allowed
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    # Get user input for the guess
    guess = int(input("Enter your guess (between 1 and 10): "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Attempts remaining: {remaining_attempts}")

# If all attempts are used without a correct guess
if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
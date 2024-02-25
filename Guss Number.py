import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of attempts
attempts = 0

# Welcome message
print("Welcome to the Number Guessing Game!")
print("I've selected a random number between 1 and 100. Try to guess it.")

# Game loop
while True:
    # Get the player's guess
    guess = int(input("Enter your guess: "))
    
    # Increment the attempts
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

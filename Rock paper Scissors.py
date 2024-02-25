import random

# Define choices
choices = ["rock", "paper", "scissors"]

# Get user's choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Validate user input
while user_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    user_choice = input("Choose rock, paper, or scissors: ").lower()

# Generate computer's choice
computer_choice = random.choice(choices)

# Display choices
print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}\n")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time.")

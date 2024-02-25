import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").upper()

        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1

    print(f"The computer guessed the number {guess} correctly!")

computer_guess(100)

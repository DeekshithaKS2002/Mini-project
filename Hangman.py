import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("Guess the word:", guessed_word)

        if guessed_word == word:
            return "Congratulations! You guessed the word correctly!"

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            tries -= 1
            print("Wrong guess. You have", tries, "tries left.")

    return "Oops! You ran out of tries. The word was " + word + "."

print(hangman())

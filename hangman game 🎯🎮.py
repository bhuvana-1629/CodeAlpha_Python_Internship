import random

words = ["apple", "mango", "tiger", "chair", "robot"]

word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("💀 You Lost!")
    print("The word was:", word);
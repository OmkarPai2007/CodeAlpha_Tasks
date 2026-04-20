import random

# Predefined list of words
words = ["apple", "tiger", "pizza", "plant", "earth"]

# Select a random word
word = random.choice(words)

guessed = []
wrong_guesses = 0
max_wrong = 6

# Create blank display
display = ["_"] * len(word)

# Game loop
while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Enter a letter: ")

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_wrong - wrong_guesses)

# Result
if "_" not in display:
    print("\nYou Win! The word is:", word)
else:
    print("\nYou Lose! The word was:", word)

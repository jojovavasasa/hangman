import random
import time

words = ["java", "hangman", "fun", "epic", "where", "python", "coding", "gaming", "winner", "help", "cheese", "pizza", "jazz", "mcdonalds", "cheeseburger", "happy", "minions"]

word_to_guess = random.choice(words)
tries = 6
word_display = ["_"] * len(word_to_guess)

while tries > 0:
    print(" ".join(word_display))
    
    guess = input().lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please input one letter.")
        continue
    
    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                word_display[i] = guess
        if "".join(word_display) == word_to_guess:
            print(f"Good job! The word was {word_to_guess}")
            break
    else:
        tries -= 1
        print(f"Wrong, try again. You have {tries} attempts left.")
        time.sleep(5)
    
if tries == 0:
    print(f"You lost. The word was {word_to_guess}")
    time.sleep(5)

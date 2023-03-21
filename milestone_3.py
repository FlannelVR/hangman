import random

word_list = ["mango", "banana", "apple", "cherry", "peach"]

word = (random.choice(word_list))
print(word)

guessed_letters = []

def check_guess(guess, word, guessed_letters):
    if guess in guessed_letters:
        print("You already guessed that letter! Try again.")
    elif guess.isalpha() and len(guess) == 1 and guess in word:
        guessed_letters.append(guess)
        print(f"Good guess! {guess} is in the word.")
        return True
    elif guess.isalpha() and len(guess) == 1:
        print(f"Sorry, {guess} is not in the word. Try again.")
        guessed_letters.append(guess)
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    return False

def ask_for_input():
    guess = input("Enter a letter: ")
    guess = guess.lower()
    return guess

while True:
    guess = ask_for_input()
    if check_guess(guess, word, guessed_letters):
        break

import random

word_list = ["mango", "banana", "apple", "cherry", "peach"]

word = (random.choice(word_list))
print(word)
guessed_letters = []

while True:
    print("Enter a letter")
    guess = input()
    if guess in guessed_letters:
        print("You already guessed that letter! Try again.")
    elif guess.isalpha() and len(guess) == 1 and guess in word:
        guessed_letters.append(guess)
        print("Good guess! {guess} is in the word."),
        break
    elif guess.isalpha() and len(guess) == 1:
        print("Sorry, {guess} is not in the word. Try again."),
        guessed_letters.append(guess),
    else:
        print("Invalid letter. Please, enter a single alphabetical character."),
import random

word_list = ["mango", "banana", "apple", "cherry", "peach"]

word = (random.choice(word_list))

hangman = True

while hangman == True:
    print("Enter a letter")
    guess = input()
    if guess.isalpha() and len(guess) == 1:
        print("Good Guess!"),
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
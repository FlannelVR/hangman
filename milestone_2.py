import random

word_list = ["mango", "banana", "apple", "cherry", "peach"]
print(word_list)

word = (random.choice(word_list))
random.choice

print("Enter a letter")
guess = input()
if guess.isalpha() and len(guess) == 1:
    print("Good Guess!"),
else:
    print("Oops! That is not a valid input")
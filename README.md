# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 2
- Task 1 - In this task I created the milestone_2.py file.
```python
"""touch milestone_2.py"""
```
I then created the 'word_list' variable and assigned a list to it with my favourite fruits and printed the output.
```python
"""word_list = ["mango", "banana", "apple", "cherry", "peach"]
print(word_list)"""
```
After saving my code I added the 'milestone_2.py' file to the git repository, commited the change with an explination and pushed to the update to the repository.
```python
"""git add milestone_2.py
git commit -m "Prints list of favourite fruits" 
git push"""
```
- Task 2 - For this task I imported the random module at the start of my 'milestone_2.py' script so that I can call this function later.
```python
"""import random"""
```
I then on the line below my list variable assigned a random word from the list using the 'random.choice' function to a new variable called 'word' and run the function to check it works.
```python
"""word = (random.choice(word_list))
random.choice"""
```
- Task 3 - I asked the user to 'Enter a letter' and added an 'input()' function to receive this input and store into a variable called 'guess'
```python
"""print("Enter a letter")
guess = input()"""
```
- Task 4 - Next I needed to validate the users response and make sure that it was a single letter in length and not any other number or character.
I also needed to print the correct output using an 'if' and 'else' statement after checking the correct conditions.
I used the 'isalpha()' function to check for letters from the alphabet as input and the 'len()' function to check the 'guess' variable was equal to the length of one letter.
```python
"""print("Enter a letter")
guess = input()
if guess.isalpha() and len(guess) == 1:
    print("Good Guess!"),
else:
    print("Oops! That is not a valid input")"""
```
# Maggie Cloos
# Module 4 assignment

from sys import exit
from random import randint


# Start here
# Creates a dictionary
myData = {}
# defines the variable guesses as equal to 0
guesses = 0
# defines the variable wins as equal to 0
wins = 0

# using a context manager open questions.txt as infile
with open("questions.txt", "r") as infile:
# read all the lines in questions.txt
    questions = infile.readlines()
# for each question in questions.txt
    for question in questions:
# if the string "first" is in the question
        if "first" in question:
# input first name
            myData["first_name"] = input(question)
# unless the string "last" is in the question
        elif "last" in question:
# then input last name
            myData["last_name"] = input(question)
"""
if there is no first or last display "bad question in input file"
and exit the game
"""
        else:
            print("bad question in input file")
            exit()

# sets game as 10 plays
for play in range(10):
# defines number as a random integer from 0-100
    number = randint(0, 100)
# if solved is false
    solved = False
# while the number is not solved
    while not solved
# prompts "Guess a number from 0 to 100" & converts guess input string to integer
        guess = int(input(f"Guess a number from 0 to 100 : "))
# add 1 to number of guesses
        guesses += 1
# if guess equals a number that has already been defined
        if guess == number:
# displays "great job [player's first name], your guess of ___ is correct"
            print(f"great job {myData["first_name"], your guess of [guess] is correct")
# add 1 to number of wins
            wins += 1
# if solved is true
            solved = True
# break out of the function
            break
"""
if the guess does not equal the number
display "your guess of __ is incorrect"
"""
        if guess != number:
            print(f"your guess of [guess] is incorrect!")

"""
if the guess is greater than the number
display "sorry, you guess too high"
"""
        if guess > number:
            print(f"Sorry, you guessed too high!")
"""
if the guess is less than the number
display "sorry, your guess is too low!"
if the guess is anything else, skip the function
"""
        elif guess < number:
            print(f"Sorry, your guess too low!")
        else:
            pass


"""
if the number is solved
display "let's play again, you have completed [# of wins] out of 10 plays"
continue on to print functions
"""
    if solved:
        print(f"Let's play again, you have completed [wins] out of 10 plays.")
        continue

# displays "[player first name & last name] guessed the correct number __ out of 10 plays"
print(f"[myData["first_name"]} {myData["last_name"]} guessed the correct number [wins] out of 10 plays.")
# displays "[player first & last name] __ guesses to do this"
print(f"It took [myData["first_name"]} {myData["last_name"]} [guesses] guesses to do this.")
# exit the game
exit()


        

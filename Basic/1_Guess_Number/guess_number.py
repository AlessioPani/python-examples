# This is a program which randomly chooses a number to guess and then 
# the user will have a few chances to guess the number correctly. 
# In each wrong attempt, the computer will give a hint that the number
# is greater or smaller than the one you have guessed.
# The user can choose the difficult of the game: this choise 
# change the range of the number randomly generated and the 
# number of attempts. 

import random


class SkillException(Exception): 
    # Exception for invalid parameter
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "{} is an invalid parameter: ".format(self.value) + \
                "are only accepted 'S' or 'C'!"


def number_generation(skill):
    # Generate a number according to the skill selected by the user. 
    if skill.upper() == 'S':
        min, max = 0, 10  # Range in the simple case
        attempts = 4 
    elif skill.upper() == 'C':
        min, max = 0, 50  # Range in the complex case
        attempts = 8
    else:
        raise SkillException(skill.upper()) 
    num_guess = random.randint(min, max)
    return num_guess, attempts


def compare_numbers(value1, value2):
    # Compare two numbers and return the result of the comparison
    if value1 == value2:
        return NUMBERS_ARE_EQUAL
    elif value1 > value2:
        return NUMBER_GREATER
    else:
        return NUMBER_LOWER


if __name__ == "__main__":
    DEBUG = 0  # For debug print
    NUMBERS_ARE_EQUAL, NUMBER_GREATER, NUMBER_LOWER = 0, 1, 2 

    skill = input("Do you want a simple or a complex game? [s, c]\n=> ")
    num_guess, attempts = number_generation(skill) 

    if DEBUG:  # If debug = 1 prints the number to guess and the attempts
        print(num_guess, attempts)

    for attempt in range(0, attempts):
        # Loop for the number of attempts and asks at the user to input
        # his value and check if it is the number generated or not, with
        # a print of an hint to help the user.
        value = int(input("\nInsert your {0:d}° value: ".format(attempt + 1)))
        retValue = compare_numbers(value, num_guess)
        if retValue == NUMBERS_ARE_EQUAL:
            print("You won! The number generated " \
                    "was {0:d}!".format(num_guess))
            break
        elif retValue == NUMBER_GREATER:
            print("=> Nope, your value is greater than the " \
                    "number to guess!", end = ' ')
        elif retValue == NUMBER_LOWER:
            print("=> Nope, your value is lower than the " \
                    "number to guess!", end = ' ')

        if attempt == attempts - 1:  # If it is the last attempt print
            print("Game over!")      # the "Game over!" message.
        else:
            print("Try again!")
            
    
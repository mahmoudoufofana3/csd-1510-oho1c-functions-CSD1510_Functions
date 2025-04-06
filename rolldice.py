#Write a function that takes as input number of dice and number of sides. The function will then return a list
#of randomly generated numbers in the proper count and range. For example if the the function is asked to generate
#3D6 or three sixed sided dice, then a potential output would be [2,2,6]
#This function cannot have any input or print statements.
#Write supporting code that will as the user for number of dice and sides, call the function, then report the results.
#The function should not be called if number of dice is zero or less and instead should report bad input to the user
#The function should not be called if number of sides is 1 or less and instead should report bad input to the user
#Sample outputs (your text does not have to match exactly)

# How many dice to roll? 3
# How many sides? 6
# Here are the results: [6, 1, 6]

# How many dice to roll? 0
# How many sides? 5
# Error: Sides must be greater than 1 and dice count greater than 0.

# How many dice to roll? 20
# How many sides? 20
# Here are the results: [18, 19, 6, 8, 13, 6, 6, 6, 18, 12, 20, 10, 14, 8, 14, 17, 12, 15, 20, 17]

import random

def roll_dice(num_dice, num_sides):
    return [random.randint(1, num_sides) for _ in range(num_dice)]

# Supporting code
try:
    num_dice = int(input("How many dice to roll? "))
    num_sides = int(input("How many sides? "))

    if num_dice <= 0 or num_sides <= 1:
        print("Error: Sides must be greater than 1 and dice count greater than 0.")
    else:
        results = roll_dice(num_dice, num_sides)
        print("Here are the results:", results)
except ValueError:
    print("Error: Please enter valid integers for dice and sides.")

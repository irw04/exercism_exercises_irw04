"""Module displaying work of loops, arithmatic, and properly written code"""

def square(number):
    """Know the number of grains for a specific square on the chess board"""
    count = 1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    for sub in range(1, number):
        count =+ 2 ** sub
    return count

def total():
    """Know the number of grains for all squares on a chess board"""
    count = 1
    for sub in range(1, 64):
        count += 2 ** sub
    return count
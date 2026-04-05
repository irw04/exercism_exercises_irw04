"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
import statistics

def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    pass


def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False

def card_average(hand):
    total = 0
    for number in hand:
        total += number
    average = total / len(hand)
    return average

def approx_average_is_average(hand):
    first_avg = (hand[0] + hand[-1]) / 2
    true_avg = sum(hand) / len(hand)

    third_avg = hand[int((len(hand)) / 2)] 
    if first_avg == true_avg:
        return True
    elif true_avg == int(third_avg):
        return True
    else:
        return False

def average_even_is_average_odd(hand):
    odd = hand[0::2]
    even = hand[1::2]
    if len(even) == 0 or len(odd) == 0:
        return False
    odd_average = sum(odd) / len(odd)
    even_average = sum(even) / len(even)
    if odd_average == even_average:
        return True
    return False
        
def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand

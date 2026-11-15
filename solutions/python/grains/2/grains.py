def square(number):
    count = 1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    for sub in range(1, number):
        count =+ 2 ** sub
    return count

def total():
    count = 1
    for sub in range(1, 64):
        count += 2 ** sub
    return count
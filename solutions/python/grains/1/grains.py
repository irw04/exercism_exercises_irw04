def square(number):
    count = 1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    for i in range(1, number):
        count =+ 2 ** i
    return count

def total():
    count = 1
    for i in range(1, 64):
        count += 2 ** i
    return count
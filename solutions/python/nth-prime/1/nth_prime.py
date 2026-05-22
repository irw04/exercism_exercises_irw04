import math

def prime(number):
    count = 0
    candidate = 1 
    if number <= 0:
        raise ValueError('there is no zeroth prime')
    while count < number:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
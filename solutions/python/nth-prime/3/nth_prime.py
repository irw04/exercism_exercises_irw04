import math 

def prime(number):
    primes = [2]
    count = 2
    if number < 1:
        raise ValueError("there is no zeroth prime")
    while len(primes) < number: 
        count += 1
        if all(count % ite > 0 for ite in primes):
            primes.append(count)

    return primes[number -1 ]
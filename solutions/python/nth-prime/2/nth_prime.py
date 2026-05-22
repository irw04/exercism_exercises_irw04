import math 

def prime(number):
    prime = [2]
    count = 2
    if number < 1:
        raise ValueError("there is no zeroth prime")
    while len(prime) < number: 
        count += 1
        if all(count % ite > 0 for ite in prime):
            prime.append(count)

    return prime[number -1 ]
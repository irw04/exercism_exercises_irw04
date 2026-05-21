def square_of_sum(number):
    total = 0 
    for i in range(0, number + 1):
        total += i
    return total*total
        
def sum_of_squares(number):
    total = 0 
    for i in range(0, number + 1):
        total += i*i
    return total

def difference_of_squares(number):
    sum = 0
    square = 0
    for i in range(0, number + 1):
        sum += i
    sum = sum * sum
    for i in range(0, number + 1):
        square += i*i
    return sum - square
    
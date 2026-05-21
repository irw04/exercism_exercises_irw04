def square_root(number):
    new_num = 0 
    for new_num in range(0, 9999):
        if new_num * new_num == number:
            return new_num
        continue
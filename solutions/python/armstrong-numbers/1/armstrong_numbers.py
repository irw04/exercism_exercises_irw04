def is_armstrong_number(number):
    numlen = len(str(number))
    new_number = 0
    for i in str(number):
        a = int(i) ** int(numlen)
        new_number += a
    if number == new_number:
        return True
    else: 
        return False
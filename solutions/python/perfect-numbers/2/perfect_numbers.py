def classify(number):
    aliquot = 0

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    for i in range(1, number):
        if number % i == 0:
            aliquot += i
    if aliquot > number:
        return "abundant"
    if aliquot < number:
        return "deficient"
    return "perfect"
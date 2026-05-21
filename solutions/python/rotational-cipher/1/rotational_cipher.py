def rotate(text, key):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    code_word = ""
    
    for letter in text:
        if letter in lower_alphabet:
            index = lower_alphabet.find(letter)
            code_word += lower_alphabet[(index + key) % 26]
        elif letter in upper_alphabet:
            index = upper_alphabet.find(letter)
            code_word += upper_alphabet[(index + key) % 26]
        else:
            code_word += letter
            
    return code_word
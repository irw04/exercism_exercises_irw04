def reverse(text):
    reversed_text = ""
    for letter in range(len(text) - 1, -1, -1):
        reversed_text += text[letter]
    return reversed_text
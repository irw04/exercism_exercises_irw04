def translate(text):
    vowel = [ "a", "e", "i", "o", "u" ]
    consonants = [ "b", "c", "d", "f", "g", "h", "j",
                  "k", "l", "m", "n", "p", "q", "r",
                  "s", "t", "v", "w", "x", "y", "z" ]
    words = text.lower().split()
    pig_latin_words = []

    split_in = 0
    """rule 1"""
    for word in words:
        if text[0] in vowel:
            pig_latin_words.append(text + "ay")
        elif text[0:2] == "yt" or text[0:2] == "xr":
            pig_latin_words.append(text + "ay")
            """rule 2 and rule 3"""
        else:
            vowel_index = 0
            for i, char in enumerate(word):
                if char in vowel:
                    vowel_index = i
                    if char == 'u' and i > 0 and word[i-1] == 'q':
                        continue
                    break
                if char == 'y' and i > 0:
                    vowel_index = i
                    break
            else:
                pig_latin_words.append(word + "ay")
                continue
            new_word = word[vowel_index:] + word[:vowel_index] + "ay"
            pig_latin_words.append(new_word)
    return " ".join(pig_latin_words)